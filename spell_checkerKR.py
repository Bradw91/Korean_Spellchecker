import requests
import urllib 
import json 

def korean_spellchecker(q):
  url = f"https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy?_callback=window.mycallback&q={q}&where=nexearch&color_blindness=0&_=1592603030513"
  
  response = requests.get(url).text
  json_string = response.replace('window.mycallback(','').replace(');','')

  result = json.loads(json_string)
  result = result['message']['result']['notag_html']

  return result


if __name__ == "__main__":
  input = input("검사하고 싶은 문장을 입력해주세요: ")
  print('검사결과: ' + korean_spellchecker(input))