from data_loader import DataLoader
from data_processor import DataProcessor
from visualizer import Visualizer
from report_generator import ReportGenerator

HISTORY_FOLDER_PATH = 'history/'
TEMPLATES_FOLDER_PATH = 'templates/'
OUTPUT_PATH = 'reports/report.html'

def main():
    loader = DataLoader(HISTORY_FOLDER_PATH)
    data = loader.load_data()

    # print(data)

    processor = DataProcessor(data)

    loot_per_character = processor.calculate_loot_per_character()

    visualizer = Visualizer(loot_per_character)
    loot_chart_path = visualizer.generate_stacked_bar_chart()

    report_generator = ReportGenerator(TEMPLATES_FOLDER_PATH)
    report_generator.generate_report({'loot_distribution_chart': loot_chart_path}, OUTPUT_PATH)

if __name__ == "__main__":
    main()