# [level 0] 배열 비교하기 - 181856 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181856) 

### 성능 요약

메모리: 9 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 04월 28일 18:44:22

### 문제 설명

<p style="user-select: auto !important;">이 문제에서 두 정수 배열의 대소관계를 다음과 같이 정의합니다.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.</li>
<li style="user-select: auto !important;">배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 다르다면 더 큰 쪽이 크고, 같다면 같습니다.</li>
</ul>

<p style="user-select: auto !important;">두 정수 배열 <code style="user-select: auto !important;">arr1</code>과 <code style="user-select: auto !important;">arr2</code>가 주어질 때, 위에서 정의한 배열의 대소관계에 대하여 <code style="user-select: auto !important;">arr2</code>가 크다면 -1, <code style="user-select: auto !important;">arr1</code>이 크다면 1, 두 배열이 같다면 0을 return 하는 solution 함수를 작성해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr1</code>의 길이 ≤ 100</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr2</code>의 길이 ≤ 100</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr1</code>의 원소 ≤ 100</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr2</code>의 원소 ≤ 100</li>
<li style="user-select: auto !important;">문제에서 정의한 배열의 대소관계가 일반적인 프로그래밍 언어에서 정의된 배열의 대소관계와 다를 수 있는 점에 유의해주세요.</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">arr1</th>
<th style="user-select: auto !important;">arr2</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[49, 13]</td>
<td style="user-select: auto !important;">[70, 11, 2]</td>
<td style="user-select: auto !important;">-1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[100, 17, 84, 1]</td>
<td style="user-select: auto !important;">[55, 12, 65, 36]</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[1, 2, 3, 4, 5]</td>
<td style="user-select: auto !important;">[3, 3, 3, 3, 3]</td>
<td style="user-select: auto !important;">0</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 1번에서는 <code style="user-select: auto !important;">arr1</code>의 길이는 2이고 <code style="user-select: auto !important;">arr2</code>의 길이는 3으로 <code style="user-select: auto !important;">arr2</code>의 길이가 더 깁니다. 따라서 <code style="user-select: auto !important;">arr2</code>가 <code style="user-select: auto !important;">arr1</code>보다 크므로 -1을 return 합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 2번에서는 <code style="user-select: auto !important;">arr1</code>의 길이과 <code style="user-select: auto !important;">arr2</code>의 길이가 4로 같습니다. <code style="user-select: auto !important;">arr1</code>의 모든 원소의 합은 100 + 17 + 84 + 1 = 202이고 <code style="user-select: auto !important;">arr2</code>의 모든 원소의 합은 55 + 12 + 65 + 36 = 168으로 <code style="user-select: auto !important;">arr1</code>의 모든 원소의 합이 더 큽니다. 따라서 <code style="user-select: auto !important;">arr1</code>이 <code style="user-select: auto !important;">arr2</code>보다 크므로 1을 return 합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #3</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 3번에서는 <code style="user-select: auto !important;">arr1</code>의 길이와 <code style="user-select: auto !important;">arr2</code>의 길이가 5로 같고 각 배열의 모든 원소의 합 또한 15로 같습니다. 따라서 <code style="user-select: auto !important;">arr1</code>과 <code style="user-select: auto !important;">arr2</code>가 같으므로 0을 return 합니다.</li>
</ul>

<hr style="user-select: auto !important;">

<p style="user-select: auto !important;">※ 공지 - 2023년 4월 21일 테스트케이스가 추가되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges