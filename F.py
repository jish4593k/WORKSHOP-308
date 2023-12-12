#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define ROCK 1
#define PAPER 2
#define SCISSOR 3

char *NAMES[] = {"", "Rock", "Paper", "Scissor"};
int WHAT_BEATS_WHAT[] = {0, 3, 1, 2};
char *WIN_ACTIONS[] = {"", "crushes", "smothers", "cuts"};

int score_player = 0;
int score_computer = 0;
int score_ties = 0;

void intro(char *player_name);
int main_loop(char *player_name);
int get_player_input();
void check_result(int player, int computer, char *player_name);
int ask_play_again(char *player_name);
void summary(char *player_name);

int main() {
    char player_name[50];
    intro(player_name);
    while (main_loop(player_name)) {
        // Do nothing, just continue the game loop
    }
    summary(player_name);
    return 0;
}

void intro(char *player_name) {
    printf("\nWelcome to Rock, Paper, and Scissor game :)\n\n");
    printf("Enter your name: ");
    scanf("%s", player_name);
}

int main_loop(char *player_name) {
    int player = get_player_input();
    int computer = 1 + rand() % 3;
    check_result(player, computer, player_name);
    return ask_play_again(player_name);
}

int get_player_input() {
    int player;
    while (1) {
        printf("\n1) Rock\n2) Paper\n3) Scissor\n");
        printf("Enter your choice: ");
        scanf("%d", &player);
        if (player >= 1 && player <= 3) {
            return player;
        } else {
            printf("Wrong choice, try again\n");
        }
    }
}

void check_result(int player, int computer, char *player_name) {
    if (player == computer) {
        printf("\nIt's a TIE! Computer also chose %s\n", NAMES[computer]);
        score_ties++;
    } else if (WHAT_BEATS_WHAT[player] == computer) {
        printf("\n%s WON! %s's %s %s Computer's %s\n", player_name, player_name, NAMES[player], WIN_ACTIONS[player], NAMES[computer]);
        score_player++;
    } else {
        printf("\nComputer WON! Computer's %s %s %s's %s\n", NAMES[computer], WIN_ACTIONS[computer], player_name, NAMES[player]);
        score_computer++;
    }
}

int ask_play_again(char *player_name) {
    char again;
    printf("\n%s do you want to play again? (y/n): ", player_name);
    scanf(" %c", &again);
    return (again == 'y');
}

void summary(char *player_name) {
    printf("\nThank You! for playing :)\n");
    printf("The results are:\n\n");
    printf("%s Won: %d\n", player_name, score_player);
    printf("Computer Won: %d\n", score_computer);
    printf("Ties: %d\n\n", score_ties);
}
