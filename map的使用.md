# map 的使用

+ 定义

  >```c++
  >map<int, string> mapStu1;
  >```
  >
  >```c++
  >typedef map<int, string> mapType;
  >mapType mapStu2, mapStu3, mapStu4;
  >```

+ 插入

  > ```c++
  > mapStu3.insert(make_pair<int, string>(1, "Qin"));
  > mapStu3.insert(make_pair<int, string>(2, "Sun"));
  > ```
  >
  > ```c++
  > mapStu4[1] = "Qin";
  > mapStu4[2] = "Sun";
  > ```
  
+ 遍历

  > ```c++
  > map<int, string>::iterator iter = mapStu.begin();
  > for (; iter != mapStu.end(); ++iter)
  > {
  > cout << "key: " << iter->first << " value: " << iter->second << endl;
  > }
  > cout << endl;
  > ```
  >
  > ```c++
  > int nSize = mapStu.size();
  > cout << "size: " << mapStu.size() << endl;
  > // 迭代map容器中的数据
  > for(int nIndex = 1; nIndex < nSize + 1; ++nIndex)
  > {
  > cout << "<" << nIndex << " :: " << mapStu[nIndex] << ">" << endl;
  > }
  > ```
  
+ 查询

  > ```c++
  > //使用find，返回的是被查找元素的位置，没有则返回map.end()。
  > map<int,string>map1;
  > if(map1.find(10)!=map1.end())
  > ```

+ 排序

+ 实例1

  >```c++
  >fstream txt;
  >txt.open(Charsfile);
  >string str;
  >while(!txt.eof()){
  >    getline(txt,str);
  >    for(int i=0;i<str.size();i++){
  >        char_frequency[str[i]]++;
  >    }
  >}
  >txt.close();
  >map<char,int>::iterator it;
  >it = char_frequency.begin();
  >while (it!=char_frequency.end())
  >{
  >    cout<<it->first<<"   "<<it->second<<endl;
  >    it++;
  >}
  >```

