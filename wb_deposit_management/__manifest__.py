{
    'name':'Deposit Management System Tutorial',
    'version': '14.0.1.0',
    'author': 'Weblearns',
    'summary': "Here you can use banking system's deposit management system, "
               "like multiple banks handle, customers profile and its balance, "
               "transaction details and notification you can send also print "
               "transaction recepit.",
    'sequence': -111,
    'description':"Here you can use banking system's deposit management system, "
               "like multiple banks handle, customers profile and its balance, "
               "transaction details and notification you can send also print "
               "transaction recepit.",
    'category':'Tutorials',
    'website':'https://freeweblearns.blogspot.com',
    'depends':['base', 'contacts', 'mail'],
    'data':[
        "data/sequence_data.xml",
        "security/ir.model.access.csv",
        "security/group_view.xml",
        "views/wb_bank_view.xml",
        "views/wb_bank_transactions_view.xml",
        "views/wb_customer_view.xml",
        "report/wb_bank_transaction_report.xml"
    ],
    'application':True

}