# [level 0] 더 크게 합치기 - 181939 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181939?language=python3) 

### 성능 요약

메모리: 9.37 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 04월 02일 16:53:00

### 문제 설명

<p style="user-select: auto !important;">연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">12 ⊕ 3 = 123</li>
<li style="user-select: auto !important;">3 ⊕ 12 = 312</li>
</ul>

<p style="user-select: auto !important;">양의 정수 <code style="user-select: auto !important;">a</code>와 <code style="user-select: auto !important;">b</code>가 주어졌을 때, <code style="user-select: auto !important;">a</code> ⊕ <code style="user-select: auto !important;">b</code>와 <code style="user-select: auto !important;">b</code> ⊕ <code style="user-select: auto !important;">a</code> 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.</p>

<p style="user-select: auto !important;">단, <code style="user-select: auto !important;">a</code> ⊕ <code style="user-select: auto !important;">b</code>와 <code style="user-select: auto !important;">b</code> ⊕ <code style="user-select: auto !important;">a</code>가 같다면 <code style="user-select: auto !important;">a</code> ⊕ <code style="user-select: auto !important;">b</code>를 return 합니다.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">a</code>, <code style="user-select: auto !important;">b</code> &lt; 10,000</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">a</th>
<th style="user-select: auto !important;">b</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">9</td>
<td style="user-select: auto !important;">91</td>
<td style="user-select: auto !important;">991</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">89</td>
<td style="user-select: auto !important;">8</td>
<td style="user-select: auto !important;">898</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">a</code> ⊕ <code style="user-select: auto !important;">b</code> = 991 이고, <code style="user-select: auto !important;">b</code> ⊕ <code style="user-select: auto !important;">a</code> = 919 입니다. 둘 중 더 큰 값은 991 이므로 991을 return 합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">a</code> ⊕ <code style="user-select: auto !important;">b</code> = 898 이고, <code style="user-select: auto !important;">b</code> ⊕ <code style="user-select: auto !important;">a</code> = 889 입니다. 둘 중 더 큰 값은 898 이므로 898을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges