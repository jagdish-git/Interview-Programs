def sort_array(arr, days):
    arr = [x for x in arr if x.get('days')==days]
    return arr
    
    
d=[{"month":"January","days":31},{"month":"February","days":29},
    {"month":"March","days":31},{"month":"April","days":30},
    {"month":"May","days":31},{"month":"June","days":30},
    {"month":"July","days":31},{"month":"August","days":31},
    {"month":"September","days":30},{"month":"October", "days":31},
    {"month":"November","days":30}, {"month":"December","days":31}
    ]
days= 30
print(sort_array(d, days))