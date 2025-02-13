#include <SFML/Graphics.hpp>
#include <vector>
#include <ctime>
#include <cstdlib>

const int NUM_COLUMNS = 80;
const int CHAR_SIZE = 20;
const int SCREEN_WIDTH = 1920;
const int SCREEN_HEIGHT = 1080;

class MatrixColumn {
public:
    MatrixColumn(float x) : x(x), y(-10), speed(rand() % 10 + 5) {}

    void update(sf::RenderWindow& window, const sf::Font& font) {
        y += speed;
        if (y > SCREEN_HEIGHT) {
            y = -10;
            speed = rand() % 10 + 5;
        }

        sf::Text text;
        text.setFont(font);
        text.setString(static_cast<char>(rand() % 93 + 33)); // Random ASCII character
        text.setCharacterSize(CHAR_SIZE);
        text.setFillColor(sf::Color(0, rand() % 255, 0)); // Random green shade
        text.setPosition(x, y);
        window.draw(text);
    }

private:
    float x, y;
    int speed;
};

int main() {
    srand(static_cast<unsigned int>(time(0)));

    sf::RenderWindow window(sf::VideoMode(SCREEN_WIDTH, SCREEN_HEIGHT), "Matrix Effect", sf::Style::Fullscreen);
    window.setFramerateLimit(60);

    // Load font (adjust path as necessary)
    sf::Font font;
    if (!font.loadFromFile("path/to/your/font.ttf")) {
        return -1;
    }

    // Initialize columns for the effect
    std::vector<MatrixColumn> columns;
    for (int i = 0; i < NUM_COLUMNS; ++i) {
        columns.emplace_back(i * (SCREEN_WIDTH / NUM_COLUMNS));
    }

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::KeyPressed && event.key.code == sf::Keyboard::Escape) {
                window.close();
            }
        }

        window.clear(sf::Color::Black);

        for (auto& column : columns) {
            column.update(window, font);
        }

        window.display();
    }

    return 0;
}
