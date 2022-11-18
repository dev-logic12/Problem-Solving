# [level 0] n의 배수 고르기 - 120905 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120905?language=python3) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">정수 <code style="user-select: auto;">n</code>과 정수 배열 <code style="user-select: auto;">numlist</code>가 매개변수로 주어질 때, <code style="user-select: auto;">numlist</code>에서 <code style="user-select: auto;">n</code>의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">n</code> ≤ 10,000</li>
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">numlist</code>의 크기 ≤ 100</li>
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">numlist</code>의 원소 ≤ 100,000</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">n</th>
<th style="user-select: auto;">numlist</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">[4, 5, 6, 7, 8, 9, 10, 11, 12]</td>
<td style="user-select: auto;">[6, 9, 12]</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">5</td>
<td style="user-select: auto;">[1, 9, 3, 10, 13, 5]</td>
<td style="user-select: auto;">[10, 5]</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">12</td>
<td style="user-select: auto;">[2, 100, 120, 600, 12, 12]</td>
<td style="user-select: auto;">[120, 600, 12, 12]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">numlist</code>에서 3의 배수만을 남긴 [6, 9, 12]를 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">numlist</code>에서 5의 배수만을 남긴 [10, 5]를 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #3</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">numlist</code>에서 12의 배수만을 남긴 [120, 600, 12, 12]를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges