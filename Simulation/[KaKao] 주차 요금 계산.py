from collections import defaultdict
def solution(fees, records):
    fee_dict = defaultdict(list)
    total_min_dict = defaultdict(int)
    caled_fee = defaultdict(int)
    
    
            
    for record in records:
        time, id, s = record.split()
        fee_dict[id].append(time)

    
    for id,time_list in fee_dict.items():
        total = 0
        for i in range(0, len(time_list)-1, 2): 
            # 5 -> 0,4,2 : 0, 2, 4 
            # 4 -> 0,3,2 : 0, 2 
            total += convert(time_list[i+1]) - convert(time_list[i])

        # 출차 안함 
        if len(time_list) % 2 == 1:
            total += convert("23:59") - convert(time_list[-1])


        total_min_dict[id] = total
        
            
    
    for id, total_min in total_min_dict.items(): 
        default_time = total_min - fees[0]
        if default_time <= 0:
            # fees[1]
            caled_fee[id] = fees[1]
        else:
            # fees[1] + exceed
            # fees[1]
            caled_fee[id] = fees[1]

            # + exceed
            exceed = default_time // fees[2]
            exceed_mod = default_time % fees[2]
            if exceed_mod == 0:
                caled_fee[id] += exceed * fees[3]

            else:
                caled_fee[id] += (exceed + 1) * fees[3]

    
    # sort by car_id
    # print(caled_fee)
    caled_fee = dict(sorted(caled_fee.items()))
    # print(caled_fee)
    
    return list(caled_fee.values())


def convert(time):
    h, m = time.split(":")
    return int(h)*60 + int(m)

'''
~20:11
1. Problem is...?
    - pair : IN && OUT
    - not pair : IN && 23:59
    
    
2. 

3. Brain Storming
    1. 시간-> 분으로 표현 
        def convert(time):
            h, m = time.split(":")
            return int(h)*60 + int(m)

        0600 = 6*60
        0634 = 6*60 + 34
        =============
        34

        1859 = 18*60 + 59
        2359 = 23*60 + 59
        =================
        5*60 
        
    2. 자료구조 => fee_dict
        fee_dict = {
        0000:[0600, 0634,1859],
        0148:[0759,1909],
        5961:[0534, 0759,2259,2300]
        }
        
        for record in records:
            time, id, s = record.split()
            fee_dict[id].append(time)
        
            
        
    3. 누적 주차 시간 => total_min_dict
        total_min_dict = {
        0000: 334,
        0148: 670,
        5961: 146
        }
        
        for id,time_list in fee_dict.item():
            total = 0
            for i in range(0, len(time_list)-1, 2):
                total += convert(time_list[i+1]) - convert(time_list[i])

            // 출차 안함 
            if len(time_list) % 2 == 1:
                total += convert(23:59) - convert(time_list[-1])


            total_min_dict[id] = total
            
    4. 꼐산
        caled_fee = 
    
    
        default_time = total_min - fees[0]
        if default_time <= 0:
            // fees[1]
            caled_fee[k] = fees[1]
            
        else:
            // fees[1] + @
            # fees[1]
            caled_fee[k] = fees[1]
            
            # + @
            exceed_mod = default_time % fees[2]
            if exceed_mod == 0:
                caled_fee[k] += exceed_mod * fees[3]
                
            else:
                caled_fee[k] += (exceed_mod + 1) * fees[3]
    
        total_fee_dict
        

4. Summarize
    fee_dict = defaultdict(list)
    total_min_dict = defaultdict(int)
    caled_fee = defaultdict(int)
    
    
            
    for record in records:
        time, id, s = record.split()
        fee_dict[int(id)].append(time)

    
    for id,time_list in fee_dict.items():
        total = 0
        for i in range(0, len(time_list)-1, 2): 
            # 5 -> 0,4,2 : 0, 2, 4 
            # 4 -> 0,3,2 : 0, 2 
            total += convert(time_list[i+1]) - convert(time_list[i])

        // 출차 안함 
        if len(time_list) % 2 == 1:
            total += convert(23:59) - convert(time_list[-1])


        total_min_dict[id] = total
        
            
    
    for id, total_min in total_min_dict.items(): 
        default_time = total_min - fees[0]
        if default_time <= 0:
            // fees[1]
            caled_fee[id] = fees[1]
        else:
            // fees[1] + exceed
            # fees[1]
            caled_fee[id] = fees[1]

            # + exceed
            exceed_mod = default_time % fees[2]
            if exceed_mod == 0:
                caled_fee[id] += exceed_mod * fees[3]

            else:
                caled_fee[id] += (exceed_mod + 1) * fees[3]

    
    # sort by car_id
    caled_fee = sorted(caled_fee, key = lambda x : x.key())
    
    return caled_fee.value()
    
        
    
        
        
            
        

'''