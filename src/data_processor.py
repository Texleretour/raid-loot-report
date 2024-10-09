class DataProcessor:
    def __init__(self, data):
        self.data = data

    def calculate_loot_per_character(self):

        ignored_responses = [
            'Autopass',
            'Pass',
            'Butin personnel - non-échangeable',
            'Passer',
            'Transmo',
            'Personal Loot - Non tradeable',
            'Offline or RCLootCouncil not installed',
            'Need Spe 2'
        ]

        filtered_data = self.data[~self.data['response'].isin(ignored_responses)]

        loot_counts = filtered_data.groupby(['player', 'response']).size().unstack(fill_value=0)

        column_order = ['Need'] + [col for col in loot_counts.columns if col != 'Need']
        loot_counts = loot_counts[column_order]

        loot_counts['Total Loots'] = loot_counts.sum(axis=1)
    
        loot_counts = loot_counts.sort_values(by='Total Loots', ascending=False)
        
        loot_counts = loot_counts.drop(columns=['Total Loots'])
            
        return loot_counts