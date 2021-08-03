from finanace_db.common_external_libs import *

class asset_class:

    def __init__(self, new=True, db='findb.sqlite',
                 name=None, asset_subclass='-', currency_name='RUB', provider_name='-', purchase_price=0, current_price=0):
        #Class initialization
        self.db=db
        if new == True:
            self.name=name
            self.asset_subclass=asset_subclass
            self.currency_name=currency_name
            self.provider_name=provider_name
            self.purchase_price=purchase_price
            self.current_price=current_price
            self.class_from_subclass()
            #If depending on type
            self.write_to_DB() #Remove?
        else: #read from DB
            pass

    def class_from_subclass(self):
        #Returns asset class of subclass
        self.asset_class='-'
        #define assets class and subclass relationship
        class_subclasses = {
            'cash': ('cash', 'debit_card'),
            'real_estate': ('real_estate', 'reit'),
            'cmdty': ('cmdty_fund'),
            'bond': ('deposit', 'saving_account', 'bond_rus', 'bond_us', 'bond_int'),
            'share': ('share_rus', 'share_us', 'share_other')
        }
        for k, v in class_subclasses.items():
            if self.asset_subclass in v:
                self.asset_class=k
                break

    def write_to_DB(self):
        #writes new entry to DB
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        #Write to Category table (multiple columns)
        cur.execute('''INSERT OR IGNORE INTO Category (asset_class, asset_subclass) 
            VALUES ( ?, ? )''',
                    (self.asset_class, self.asset_subclass)
                    )
        cur.execute('SELECT id FROM Category WHERE asset_subclass = ? ',
                    (self.asset_subclass, )
                    )
        category_id=cur.fetchone()[0]

        #Write to Category table (single column)
        cur.execute('''INSERT OR IGNORE INTO Provider (name) 
            VALUES ( ?)''',
                    (self.provider_name, )
                    )
        cur.execute('SELECT id FROM Provider WHERE name = ? ',
                    (self.provider_name, )
                    )
        provider_id=cur.fetchone()[0]

        #Write to Currency table
        cur.execute('''INSERT OR IGNORE INTO Currency (name) 
            VALUES ( ?)''',
                    (self.currency_name, )
                    )
        cur.execute('SELECT id FROM Currency WHERE name = ? ',
                    (self.currency_name, )
                    )
        currency_id=cur.fetchone()[0]

        #Write to (master) Asset table
        cur.execute('''INSERT OR IGNORE INTO Asset (name, purchase_price, current_price, category_id, provider_id, currency_id) 
            VALUES ( ?, ?, ?, ?, ?, ?)''',
                    (self.name, self.purchase_price, self.current_price, category_id, provider_id, currency_id)
                    )

        conn.commit()
        cur.close()