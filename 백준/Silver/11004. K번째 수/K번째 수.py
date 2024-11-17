#백준 11004문제 ( K번째 수 )
N, K = map(int,input().split())  # N개의 수, 오름차순 후 K번째의 수를 정렬
arr = list(map(int,input().split())) # 리스트로 들어가게
arr.sort()  # 오름차순 정렬
print(arr[K-1]) # 인덱스 0부터 시작이여서 -1