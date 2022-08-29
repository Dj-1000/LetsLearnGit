#include<iostream>
using namespace std;
int add(int a, int b){
    return a+b ; 
}
int main(){
  int a=0 ,b=0;
  cout<<" Enter any two : ";
  cin>> a >> b;
  cout<<"Addition of the two :";
  cout<< add(a, b);
  return 0;
}