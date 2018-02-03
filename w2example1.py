def logger(func):
    def wrapped(*args,**kwargs):
        result = func(*args, **kwargs)
        with open('log.txt' , 'w') as f:
            f.write(str(result))

        return result    
    return wrapped





@logger
def summator(num_list):
    return sum(num_list)

#summator([1,2,10,30])

with open('log.txt','r') as f:
    print('log.txt:{}'.format(f.read()))
