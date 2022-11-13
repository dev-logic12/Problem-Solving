# [level 0] 가까운 수 - 120890 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120890) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">정수 배열 <code style="user-select: auto;">array</code>와 정수 <code style="user-select: auto;">n</code>이 매개변수로 주어질 때, <code style="user-select: auto;">array</code>에 들어있는 정수 중 <code style="user-select: auto;">n</code>과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">array</code>의 길이 ≤ 100</li>
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">array</code>의 원소 ≤ 100</li>
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">n</code> ≤ 100</li>
<li style="user-select: auto;">가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">array</th>
<th style="user-select: auto;">n</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">[3, 10, 28]</td>
<td style="user-select: auto;">20</td>
<td style="user-select: auto;">28</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">[10, 11, 12]</td>
<td style="user-select: auto;">13</td>
<td style="user-select: auto;">12</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">3, 10, 28 중 20과 가장 가까운 수는 28입니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">10, 11, 12 중 13과 가장 가까운 수는 12입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges