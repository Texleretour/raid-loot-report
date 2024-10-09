import matplotlib.pyplot as plt

class Visualizer():
    def __init__(self, data):
        self.data = data

    def generate_stacked_bar_chart(self):

        response_color_map = {

        }

        class_color_map = {

        }

        ax = self.data.plot(kind='bar', stacked=True, figsize=(10, 6), colormap="tab20")

        ax.set_title('Distribution des loots par personnage')
        ax.set_xlabel('Personnage')
        ax.set_ylabel('Nombre de loots')

        for tick, player in zip(ax.get_xticks(), self.data.index):
            player_class = self.player_classes.get(player, 'Unknown')  # Get the player's class
            tick_color = class_color_map.get(player_class, '#000000')  # Default to black if class not found
            ax.get_xticklabels()[tick].set_color(tick_color)

        plt.tight_layout()
        plt.savefig('reports/loot_distribution.png')
        plt.close()

        return 'loot_distribution.png'