
blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_info = {
    'A': 0,
    'B': 0,
    'AB': 0,
    'O': 0,
}

for i in blood_type:
     blood_info[i] += 1

               
print(blood_info)


# 새로 등장한 키를 비어있는 딕셔너리에 추가하면서 작성

location_list = ['서울', '서울', '서울', '부산', '대전', '제주', '광주', '부산']

location_dict = {}

for location in location_list:
    # 이미 기록한 경우
    if location in location_dict.keys():
          location_dict[location] += 1
    # 처음 등장한 경우
    else:
         location_dict[location] = 1
        
print(location_dict)