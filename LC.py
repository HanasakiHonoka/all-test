import requests
import json
from string import Template
import re
import os

headers = {
        'content-type': 'application/json',
}

def gql_query(gql):
    url = "https://leetcode-cn.com/graphql/"
    headers = {
        'content-type': 'application/json',
    }
    param = {'query':gql}
    return requests.post(url, json = param, headers = headers).text


def get_question_data(questionTitleSlug):
    gql = '''
    query {  question(titleSlug: "''' + questionTitleSlug +  ''' ") 
    { questionFrontendId titleSlug codeSnippets {      lang      langSlug      code      __typename    }}}
    '''
    res = json.loads(gql_query(gql))
    question = res['data']["question"]
    title = question['titleSlug']
    question_id = question['questionFrontendId']
    java_code = ''
    for code_temp in question['codeSnippets']:
        if code_temp['lang'] == "Java":
            java_code = code_temp['code']
            break
    java_code = re.sub('''class.*''', "public class Problem" + question_id +" {", java_code)
    return title, question_id, java_code
    print(java_code)

def get_today_problem():
    gql = '''query questionOfToday{todayRecord{question{questionFrontendId, questionTitleSlug}}}'''
    res = json.loads(gql_query(gql))
    question = res['data']['todayRecord'][0]['question']
    return question['questionTitleSlug'], question['questionFrontendId']

def write_to_file(title, question_id, java_code):
    # write test code
    rf = open("D:\WorkSpace\leetcode\src\problem\LeetTest.java", 'r', encoding='utf-8')
    lines = rf.readlines()
    wf = open("D:\WorkSpace\leetcode\src\problem\LeetTest.java", 'w', encoding='utf-8')
    test_code = Template('''
    @Test
    public void problem${id}() {
        Problem${id} problem${id} = new Problem${id}();
    }''').substitute(id = question_id)
    for line in lines:
        if re.match("^}", line):
            wf.write(test_code)
            wf.write("\n")
            wf.write("}")
        else:
            wf.write(line)
    rf.close()
    wf.close()

    # create Problem code
    with open("D:\WorkSpace\leetcode\src\problem\Problem" + question_id +  ".java", 'w', encoding='utf-8') as f:
        f.write("package problem;\n//https://leetcode-cn.com/problems/{}/\n".format(title) + java_code)


def check(questionFrontendId):
    file_new = "Problem" + questionFrontendId + ".java"
    files = os.listdir("D:\WorkSpace\leetcode\src\problem")
    for file in files:
        if file == file_new:
            print("做过了" + questionFrontendId)
            return False
    return True


if __name__ == '__main__':
    questionTitleSlug, questionFrontendId = get_today_problem()
    if check(questionFrontendId):
        # print(questionTitleSlug)
        title, question_id, java_code = get_question_data(questionTitleSlug)
        # print("package problem;\n" + java_code)
        write_to_file(title, question_id, java_code)

