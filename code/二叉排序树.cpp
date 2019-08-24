#include<bits/stdc++.h>
using namespace std;

typedef struct node
{
      int data;
      node *l,*r;
}node,*tree;

void Insert(tree &t,int e){
      if(!t){
            node *s =new node;
            s->data=e;
            s->l=s->r=NULL;
            t=s;
      }
      else if(e<t->data) Insert(t->l,e);
      else if(e>t->data) Insert(t->r,e); 
      
}
void Create(tree &t){
      t=NULL;
      int e;
      cin>>e;
      while(e!=0){
            Insert(t,e);
            cin>>e;
      }
}

void Delete(tree &t,int key){
      tree p=t;
      tree f=NULL;
      while(p){
            if(p->data==key) break;
            f=p;
            if(p->data>key) p=p->l;
            else p=p->r;
      }
      if(!p){
            cout<<"没有找到\n---\n";
            return;
      }
      tree q=p;
      if((p->l)&&(p->r)){
            tree s=p->l;
            while (s->r)
            {
                  q=s;
                  s=s->r;
            }
            p->data=s->data;
            if(q!=p) q->r=s->l;
            else q->l = s->l;
            delete s;
            return;
      }
      else if(!p->r) p =p->l;
      else if(!p->l) p =p->r;
      if(!f) t=p;
      else if(q==f->l) f->l=p;
      else f->r=p;
      delete q;
      cout<<"删除成功!\n\n";
}
void Print(tree &t){
      if(t==NULL) return;
      Print(t->l);
      cout<<t->data<<" ";
      Print(t->r);
}
int main()
{
      tree t;
      cout << "请输入:          (以0结束)\n";
      Create(t);
      cout<<"输入完成\n";
      int choose=0;
      cout << "请选择以下操作:\n";
      cout << "--1.删除\n--2.中序遍历\n--3.插入新数据\n";
      while(cin>>choose){
            if(choose==1){
                  cout<<"请输入删除节点的信息\n";
                  int key=0;
                  cin>>key;
                  Delete(t,key);
            }
            if(choose==2){
                  Print(t);
                  cout<<"\n---\n";
            }
            if(choose==3){
                  cout << "请输入:          (以0结束)\n";
                  int e;
                  while(cin >> e){
                        if(e==0)break;
                        Insert(t, e);
                        cout << "插入成功\n---\n";
                  }
            }
            cout << "请选择以下操作:\n";
            cout << "--1.删除\n--2.中序遍历\n--3.插入新数据\n";
      }

}

