from django.shortcuts import render

# Create your views here.
def DBC(request):
    if request.method=='POST':
        d=request.POST
        n1=d.get('area')
        n2=d.get('peri')
        # n3=d.get('ma')
        # n4=d.get('ml')
        n3=d.get('ex')
        n4=d.get('sol')
        n5=d.get('rou')
        n6=d.get('com')
        n7=d.get('s1')
        n8=d.get('s2')
        n9=d.get('s3')
        n10=d.get('s4')
        if "btnpredict" in request.POST:
            import pandas as pd
            data=pd.read_csv('C:\\Users\\patra\\Dataset\\train_dataset.csv')
            from sklearn.preprocessing import StandardScaler
            sc=StandardScaler()
            sc.fit(data[['Area','Perimeter','MajorAxisLength','MinorAxisLength','AspectRation','Eccentricity','ConvexArea','EquivDiameter','Extent','Solidity','roundness','Compactness','ShapeFactor1','ShapeFactor2','ShapeFactor3','ShapeFactor4']])
            data[['Area','Perimeter','MajorAxisLength','MinorAxisLength','AspectRation','Eccentricity','ConvexArea','EquivDiameter','Extent','Solidity','roundness','Compactness','ShapeFactor1','ShapeFactor2','ShapeFactor3','ShapeFactor4']]=sc.transform(data[['Area','Perimeter','MajorAxisLength','MinorAxisLength','AspectRation','Eccentricity','ConvexArea','EquivDiameter','Extent','Solidity','roundness','Compactness','ShapeFactor1','ShapeFactor2','ShapeFactor3','ShapeFactor4']])
            inputs=data[['Area','Perimeter','Extent','Solidity','roundness','Compactness','ShapeFactor1','ShapeFactor2','ShapeFactor3','ShapeFactor4']]
            output=data['Class']
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test= train_test_split(inputs,output,train_size=0.8)
            from sklearn.linear_model import LogisticRegression
            model=LogisticRegression(solver='lbfgs',class_weight='balanced', max_iter=10000)
            model.fit(x_train,y_train)
            result=model.predict([[float(n1),float(n2),float(n3),float(n4),float(n5),float(n6),float(n7),float(n8),float(n9),float(n10)]])
            return render(request,'DBC.html',context={'result':result})
    return render(request,'DBC.html')