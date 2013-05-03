# -*- coding: utf-8 -*-


import emilee.tagger

from emilee import emilee


testcases = [
        {"q": "프랑스의 수도는?", "a" : ["파리"]},
        {"q": "호주의 수도는?", "a": ["캔버라"]},
        {"q": "15대 대통령은?", "a": ["김대중"]},
        {"q": "아이유의 본명은?", "a": ["지은", "이지은", "지은이"]},
        {"q": "윤하의 데뷔곡은?", "a": ["유비키리", "오디션"]},
        {"q": "아이유의 데뷔곡은?", "a": ["미아"]},
        {"q": "빛의 삼원색은?", "a": ["빨강", "파랑", "노랑"]},
        #{"q": "오징어의 다리수는?", "a": ["10", "10개", "열", "열개"]},
        {"q": "모비딕의 작가는?", "a": ["허먼", "멜빌", "허먼멜빌"]},
        {"q": "신라의 수도는?", "a": ["경주", "서라벌"]},
        {"q": "한글을 만든 왕은?", "a": ["세종", "세종대왕"]},
        {"q": "모짜르트의 출생지는?", "a": ["오스트리아", "잘츠부르크"]},
        {"q": "사과의 색깔은?", "a": ["빨강", "빨강색", "빨간색"]},
        {"q": "바나나의 색깔은?", "a": ["노랑", "노랑색", "노란색"]},
        {"q": "갤럭시 S 제조사는?", "a": ["삼성", "삼성전자"]},
        {"q": "그리스의 언어는?", "a": ["그리스어"]},
        #{"q": "한글 창제 년도는?", "a": ["1446", "1446년", "1443", "1443년"]},
        {"q": "비행기를 만든 사람은?", "a": ["라이트 형제", "라이트형제", "라이트"]},
        {"q": "지면을 이루는 물질중에 가장 많은 양을 차지하는 물질은?", "a": ["산소"]},
        {"q": "한국인의 사망 원인 1위는?", "a": ["암"]},
        #{"q": "면허를 딸 수 있는 나이는?", "a": ["만 18세", "18", "18세"]},
        {"q": "세상에서 가장 긴 강?", "a": ["아마존 강", "아마존"]},
        #{"q": "물의 끓는 점 온도는?", "a": ["100도", "100"]},
        #{"q": "한국의 독립 년도는?", "a": ["1945", "1945년"]},
        {"q": "아인슈타인이 태어난 나라는?", "a": ["독일"]},
        {"q": "최초로 달에 간 사람은?", "a": ["닐 암스트롱", "암스트롱"]},
        {"q": "해바라기를 그린 화가는?", "a": ["반 고흐", "고흐"]},
        {"q": "맨체스터 유나이티드에서 활동하는 한국인 축구선수는?", "a": ["박지성"]},
        {"q": "거북선을 만든 사람은?", "a": ["이순신"]},
        {"q": "애플의 전 회장은?", "a": ["스티브 잡스", "잡스"]},
        {"q": "빌리 진을 부른 가수는?", "a": ["마이클 잭슨"]},
        {"q": "서울대학교 출신 여자 연예인은?", "a": ["김태희"]},
        {"q": "해를 품은 달 작가는?", "a" : ["진수완"]},
        {"q": "빅뱅이론에서 쉘든역을 맡은 배우는?", "a": ["짐 파슨스", "파슨스"]},
        #{"q": "에펠탑의 높이는?", "a": ["324미터", "324"]},
        {"q": "미국 대통령 이름은?", "a": ["오바마"]},
        #{"q": "한국 남성 평균 키는?", "a": ["173.3"]},
        {"q": "슈퍼스타 K 3 우승자는?", "a": ["울랄라 세션", "울랄라", "울랄라세션"]},
        {"q": "한나라당이 개명한 이름은?", "a": ["새누리당", "새누리"]},
        #{"q": "카프카의 대표작은?", "a": ["변신"]},
        {"q": "2010년 동인문학상 수상 작가는?", "a": ["김인숙"]},
        {"q": "오만과 편견을 지은 작가는?", "a": ["제인 오스틴", "오스틴", "제인"]},
        {"q": "작가 베르나르 베르베르의 국적은?", "a": ["프랑스"]},
        {"q": "겁쟁이를 부른 밴드는?", "a": ["버즈"]},
        {"q": "CCB10 우승 클랜은?", "a": ["cmax"]},
        {"q": "세계 점유율 1위 게임은?", "a": ["리그 오브 레전드"]},
        {"q": "워크래프트를 만든 회사는?", "a": ["블리자드"]},
        {"q": "기독교를 창시한 사람은?", "a": ["예수"]},
        {"q": "영화 매트릭스 주인공은?", "a": ["네오"]},
        {"q": "음의 고저가 다르게 관찰되는 현상은?", "a": ["맥놀이"]},
        {"q": "아이폰을 만든 회사는?", "a": ["애플"]},
        {"q": "반지의 제왕 감독은?", "a": ["피터 잭슨", "잭슨"]},
        {"q": "목성의 대기 성분중 가장 많은 양을 차지하는 기체는?", "a": ["수소"]},
        {"q": "원피스 작가는?", "a": ["오다 에이치로", "에이치로 오다", "에이치", "오다"]},
        {"q": "요정 컴미 주인공은?", "a": ["전성초"]},
        #{"q": "스타크래프트 마린의 체력은?", "a": ["40"]},
        {"q": "꾸러기 수비대의 주인공은?", "a": ["똘기"]},
        {"q": "애국가의 작곡가는?", "a": ["안익태"]},
        {"q": "삼성 회장은?", "a": ["이건희"]},
        {"q": "써니의 본명은?", "a": ["이순규", "순규"]},
        {"q": "김대중의 출생지는?", "a": ["신안", "전라도"]},
        {"q": "무한도전 PD 이름은?", "a": ["김태호"]},
        #{"q": "이명박의 나이는?", "a": ["68"]},
        ]



def evaluate_accuracy():
    total_count = len(testcases)
    correct_count = 0
    real_correct_count = 0


    for testcase in testcases:
        print testcase ['q'],
        ans = emilee.get_answer(testcase['q'])

        result = 'X'
        real_result = 'X'
        for ans_tup in ans[:5]:
            answer, count, pmi, total = ans_tup
            print "(%s, %d, %f, %f) " % (answer, count, pmi, total),
            if answer.encode("utf8") in testcase['a']:
                result = 'O'
                correct_count = correct_count + 1

        if len(ans) > 0:
            answer, count, pmi, total = ans[0]
            if answer.encode("utf8") in testcase['a']:
                real_correct_count += 1
                real_result = 'O'
        print " | %s , %s " % (result, real_result)

    print "%d / %d = %f" % (correct_count, total_count, correct_count/float(total_count))
    print "[real]%d / %d = %f" % (real_correct_count, total_count, real_correct_count/float(total_count))



def analyse_question():
    for testcase in testcases:
        print testcase['q'],
        print tagger.postagging(testcase['q'])





if __name__=="__main__":
    evaluate_accuracy()
    #analyse_question()