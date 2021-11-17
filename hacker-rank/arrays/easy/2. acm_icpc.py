"""
Idea က တစ်ခုချင်းစီကို ပေါင်း မှာ။ 0 နဲ့ 0 ဆို 0, 1 နဲ့ 0 ဆို 1, 1 နဲ့ 1 ဆို 2
2 ကိုတော့ 1ပြန်ပြောင်းပြီး 1 စုစုပေါင်းရှိတဲ့ အရေအတွက်ကို ရှာလိုက်တာ။

ကျောင်းသား           သူသိတဲ့ အရေအတွက် (1ဆို အဲ့subject ကို ကျောင်းသားက သိတယ် 0 ဆို မသိဘူး)
1               => 10101
2               => 11110
3               => 00010

Team            => Answers
[1, 2]          => 10101+11110 => 21211 => 11111(Change 2 to 1)=>Count of '1'
[1, 3]          => အပေါ်က လိုပဲ နှစ်ယောက်လုံးက မသိရင် 0, နှစ်ယောက်လုံးသိရင် 2, တစ်ယောက်ပဲ သိလည်း 1 Concept
[2, 3]          => အပေါ်က လိုပဲ နှစ်ယောက်လုံးက မသိရင် 0, နှစ်ယောက်လုံးသိရင် 2, တစ်ယောက်ပဲ သိလည်း 1 Concept

"""

def acmTeam(topic):
    # Write your code here
    maximum = 0
    max_val = 0
    for i in range(0, len(topic)-1):
        for j in range(i+1, len(topic)):
            
            summation = int(topic[i])+int(topic[j])
            summation = (re.sub(r'2',r'1', str(summation))).count('1')
            
            if (summation>maximum):
                maximum = summation
                max_val  = 1
            elif(summation == maximum):
                max_val  +=1 
    return [maximum, max_val]


'''I would like to update the code.

Instead of chaning from 2 to 1, count the number of '0' and then subtract from the total numbers subjects.

summation = str(int(topic[i])+int(topic[j]))

summation = len(summation) - summation.count('0')'''
