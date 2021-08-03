class_subclasses = {
    'cash': ('cash', 'debit_card'),
    'real_estate': ('real_estate', 'reit'),
    'cmdty': ('cmdty_fund'),
    'bond': ('deposit', 'saving_account', 'bond_rus', 'bond_us', 'bond_int'),
    'share': ('share_rus', 'share_us', 'share_other')
}

for k, v in class_subclasses.items():
    if 'reit' in v:
        asset_class = k
        break

print(asset_class)