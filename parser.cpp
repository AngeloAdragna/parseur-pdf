#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>
#include <regex>
#include <string>
#include <sstream>
#include <chrono>
#include <cstdlib>

namespace fs = std::filesystem;

std::string get_file_name(const fs::path& filepath) {
    return filepath.stem().string();
}

bool est_ligne_auteur(const std::string& ligne, bool is_first_line = false) {
    std::string l = std::regex_replace(ligne, std::regex("^ +| +$|( ) +"), "$1");
    if (l.empty() || is_first_line) return false;

    if (std::regex_search(l, std::regex("\\b(and|et)\\b", std::regex::icase))) {
        std::istringstream iss(l);
        std::string mot;
        bool valid = true;
        while (iss >> mot) {
            if (!(std::regex_match(mot, std::regex("^[A-Z][a-z\\-]+$")) || mot == "and" || mot == "et")) {
                valid = false;
                break;
            }
        }
        if (valid) return true;
    }

    std::smatch m;
    std::regex noms_regex("\\b[A-Z][a-z]+(?:\\s[A-Z][a-z]+)?");
    std::string::const_iterator searchStart(l.cbegin());
    int count = 0;
    while (std::regex_search(searchStart, l.cend(), m, noms_regex)) {
        count++;
        searchStart = m.suffix().first;
    }

    if (count >= 2) return true;
    if (l.find('@') != std::string::npos || l.find("university") != std::string::npos) return true;

    return false;
}

std::string extraire_titre_intelligent(const fs::path& filepath, int max_lines = 15) {
    std::ifstream file(filepath);
    std::string line;
    std::vector<std::string> lignes;
    int count = 0;
    while (std::getline(file, line) && count++ < max_lines) {
        lignes.push_back(line);
    }

    std::vector<std::string> bloc_titre;
    for (size_t i = 0; i < lignes.size(); ++i) {
        std::string l = lignes[i];
        if (l.empty()) continue;
        bool is_first_line = (i == 0);
        if (est_ligne_auteur(l, is_first_line) || std::regex_search(l, std::regex("^abstract", std::regex::icase)))
            break;
        bloc_titre.push_back(l);
    }

    std::ostringstream oss;
    for (const auto& l : bloc_titre) oss << l << " ";
    return oss.str();
}

std::vector<fs::path> list_pdfs(const fs::path& repertoire) {
    std::vector<fs::path> pdfs;
    for (const auto& entry : fs::directory_iterator(repertoire)) {
        if (entry.path().extension() == ".pdf") pdfs.push_back(entry.path());
    }
    return pdfs;
}

std::vector<std::string> get_lines(const std::string& content) {
    std::vector<std::string> lines;
    std::istringstream iss(content);
    std::string line;
    while (std::getline(iss, line)) lines.push_back(line);
    return lines;
}

std::vector<std::string> get(const std::string& content) {
    auto lines = get_lines(content);
    bool begin_found = false, end_found = false;
    size_t i = 0;

    while (i < lines.size()) {
        if (!begin_found && std::regex_match(lines[i], std::regex("^ *Abstract", std::regex::icase))) {
            lines[i] = std::regex_replace(lines[i], std::regex("^ *Abstract\\W*", std::regex::icase), "");
            lines = std::vector<std::string>(lines.begin() + i, lines.end());
            begin_found = true;
            i = 0;
        }
        if (!end_found && std::regex_match(lines[i], std::regex("^([1I]\\.? )?Introduction", std::regex::icase))) {
            lines = std::vector<std::string>(lines.begin(), lines.begin() + i);
            end_found = true;
            break;
        }
        ++i;
    }

    if (!begin_found) {
        if (lines.size() > 3) lines.erase(lines.begin(), lines.begin() + 3);
        for (size_t j = 0; j < lines.size(); ++j) {
            if (std::regex_search(lines[j], std::regex("paper|article|presents?|examines?", std::regex::icase))) {
                lines = std::vector<std::string>(lines.begin() + j, lines.end());
                break;
            }
        }
    }

    return lines;
}

std::string get_string(const std::string& text) {
    auto lines = get(text);
    std::ostringstream oss;
    for (size_t i = 0; i < lines.size(); ++i) {
        std::string line = std::regex_replace(lines[i], std::regex("^ +| +$|( ) +"), "$1");
        if (!line.empty() && !oss.str().empty() && oss.str().back() == '-') {
            std::string prev = oss.str().substr(0, oss.str().size() - 1);
            std::string first = line.substr(0, line.find(' '));
            oss.str(prev + first + line.substr(first.size()));
        } else {
            if (i > 0) oss << " ";
            oss << line;
        }
    }
    return oss.str();
}

void add_infos_to_file(const fs::path& fichier_txt) {
    std::string filename = get_file_name(fichier_txt);
    std::string titre = extraire_titre_intelligent(fichier_txt);

    std::ifstream f_in(fichier_txt);
    std::stringstream buffer;
    buffer << f_in.rdbuf();
    std::string content = buffer.str();
    f_in.close();

    std::string abstract = get_string(content);

    std::ofstream f_out(fichier_txt);
    f_out << "Nom du fichier : " << filename << "\n";
    f_out << "Titre : " << titre << "\n";
    f_out << "Abstract : " << abstract << "\n";
}

void convert_pdf_file_to_plain_text(const fs::path& fichier_pdf, const fs::path& repertoire_sortie) {
    fs::path fichier_sortie = repertoire_sortie / (fichier_pdf.stem().string() + ".txt");
    std::string cmd = "pdftotext -raw \"" + fichier_pdf.string() + "\" \"" + fichier_sortie.string() + "\"";
    int res = system(cmd.c_str());

    if (res == 0) {
        std::cout << fichier_pdf.filename() << " converti en " << fichier_sortie.filename() << std::endl;
        add_infos_to_file(fichier_sortie);
    } else {
        std::cerr << "Erreur lors de la conversion de " << fichier_pdf.filename() << std::endl;
    }
}

void pdfs_to_plain_texts(const fs::path& entree, const fs::path& sortie) {
    if (entree == sortie) {
        throw std::runtime_error("Les répertoires doivent être différents");
    }

    auto pdfs = list_pdfs(entree);
    if (fs::exists(sortie)) fs::remove_all(sortie);
    fs::create_directories(sortie);

    for (const auto& pdf : pdfs) {
        convert_pdf_file_to_plain_text(pdf, sortie);
    }
}

void log_execution_time(double duration, const fs::path& log_file = "exec_time_cpp.log") {
    std::ofstream out(log_file, std::ios::app);
    out << duration << "\n";
    out.close();

    std::ifstream in(log_file);
    std::string line;
    std::vector<double> times;
    while (std::getline(in, line)) {
        try {
            times.push_back(std::stod(line));
        } catch (...) {}
    }
    in.close();

    if (!times.empty()) {
        double avg = 0;
        for (double t : times) avg += t;
        avg /= times.size();
        std::cout << "Moyenne des temps d'exécution : " << avg << " secondes" << std::endl;
    } else {
        std::cout << "Aucune donnée valide dans le fichier de log." << std::endl;
    }
}

int main(int argc, char* argv[]) {
    auto start = std::chrono::high_resolution_clock::now();

    if (argc < 3) {
        std::cerr << "Erreur : veuillez fournir les chemins du répertoire d’entrée et de sortie." << std::endl;
        return 1;
    }

    fs::path entree(argv[1]);
    fs::path sortie(argv[2]);

    if (!fs::exists(entree) || !fs::is_directory(entree)) {
        std::cerr << "Erreur : répertoire d’entrée invalide." << std::endl;
        return 1;
    }

    auto pdfs = list_pdfs(entree);
    if (pdfs.empty()) {
        std::cout << "Aucun fichier PDF trouvé." << std::endl;
    } else {
        std::cout << "Fichiers PDF trouvés :" << std::endl;
        for (const auto& pdf : pdfs) std::cout << " - " << pdf.filename() << std::endl;
    }

    pdfs_to_plain_texts(entree, sortie);

    auto end = std::chrono::high_resolution_clock::now();
    double duration = std::chrono::duration<double>(end - start).count();
    log_execution_time(duration);

    return 0;
}
    