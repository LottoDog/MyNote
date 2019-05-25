# 输入流/输出流

>+ ##  输入流操作
>
>> + ### cin>>
>>
>> 接受一个字符串，遇“空格”、“TAB”、“回车”都结束
>>
>> + ### cin.get()
>>
>> **用法1**： ==单个接收== cin.get(字符变量名)可以用来接收字符 
>>
>> ```c++
>> #include <iostream>
>> using namespace std;
>> main ()
>> {
>> char ch;
>> ch=cin.get();   //或者cin.get(ch);
>> cout<<ch<<endl;
>> }
>> //输入:asdf
>> //输出:a
>> ```
>>
>> **用法2**：cin.get(字符数组名,接收字符数目)用来接收一行字符串,可以==接收空格==
>>
>> ```c++
>> #include <iostream>
>> using namespace std;
>> main ()
>> {
>> char a[20];
>> cin.get(a,20);
>> cout<<a<<endl;
>> }
>> //输入：jkl jkl jkl 
>> //输出：jkl jkl jkl 
>> //输入：abcdeabcdeabcdeabcdeabcde （输入25个字符）
>> //输出：abcdeabcdeabcdeabcd （接收19个字符+1个’\0’） 
>> ```
>>
>> **用法3**：cin.get(==无参数==)没有参数主要是用于==舍弃输入==流中的不需要的字符,或者舍弃回车,弥补cin.get(字符数组名,接收字符数目)的不足. 
>>
>> + ### cin.getline()
>>
>> 接受一个字符串，可以接收空格并输出
>>
>> ```c++
>> #include <iostream>
>> using namespace std;
>> main ()
>> {
>> char m[20];
>> cin.getline(m,5);
>> cout<<m<<endl;
>> }
>> /*
>> 输入：jkljkljkl
>> 　　输出：jklj
>> 接受5个字符到m中，其中最后一个为’\0’，所以只看到4个字符输出； 
>> */
>> /*
>> 延伸:
>> cin.getline()实际上有三个参数，cin.getline(接受字符串,接收个数,结束字符) 
>> 当第三个参数省略时，系统默认为’\0’ 
>> 如果将例子中cin.getline()改为cin.getline(m,5,’a’);当输入jlkjkljkl时输出jklj，输入jkaljkljkl时，输出jk 
>> */
>> ```
>>
>> + ### getline()
>>
>> 接受一个字符串，可以==接收空格并输出==
>>
>> ```c++
>> #include<iostream>
>> #include<string>
>> using namespace std;
>> main ()
>> {
>> string str;
>> getline(cin,str);
>> cout<<str<<endl;
>> }
>> /*
>> 输入：jkl jfksldfj jklsjfl
>> 输出：jkl jfksldfj jklsjfl */
>> ```
>>
>> #### <u> cin.getline()属于istream流，而getline()属于string流</u>
>>
>> + ### gets()
>>
>>   接受一个字符串，可以接收空格并输出
>>
>>   ```c++
>>   #include<iostream>
>>   #include<string>
>>   using namespace std;
>>   main ()
>>   {
>>       char m[20];
>>       gets(m);     //不能写成m=gets();
>>       cout<<m<<endl;
>>   }
>>   ```
>>
>>   [以上内容参考到的链接](https://blog.csdn.net/JIEJINQUANIL/article/details/50802902)
>
>+ ##  输出流操作
>
>+ ## 流错误状态
>
>+ ## 文件处理
>
>> + ### 打开文件
>>
>>   ```c++
>>   fstream txt;
>>   txt.open("a.txt,ios::in");
>>   string str;
>>   while(!txt.eof()){
>>       getline(txt,str);
>>   }
>>   ```
>>
>> + ### 关闭文件
>>
>>   ```c++
>>   txt.close()
>>   ```
>>
>

