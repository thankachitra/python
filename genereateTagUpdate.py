import pandas as pd



def main():
    readFile("aws_accounts.xlsx")

def readFile(filename):
    cols=["account_number","tagname"]
    data=[()]
    input_data_frame = pd.read_excel(filename)

    
    #print (data.loc[[0,1],['tagname','account_number']])
    
    for index, row in input_data_frame.iterrows():
        tagnames=row['tagname']
        account_number=row['account_number']
        tags=tagnames.split(',')
        for tag in tags:
            tagname=str(tag)+str(account_number)
            data.append((str(account_number),tagname))

    output_data=pd.DataFrame(data,index=range(len(data)),columns=cols)
    output_data.to_excel("output.xlsx")
    print (output_data)
    

""" def __init__(self, **args):
    if (args.len()==0):
        print( "insufficient arguments")
        pass
    else:
        self.fileName=args.filename.value
"""
if __name__ == "__main__":
    main()