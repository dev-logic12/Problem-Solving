# [level 0] 배열 회전시키기 - 120844 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120844) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">정수가 담긴 배열 <code style="user-select: auto;">numbers</code>와 문자열&nbsp;<code style="user-select: auto;">direction</code>가 매개변수로 주어집니다. 배열 <code style="user-select: auto;">numbers</code>의 원소를 <code style="user-select: auto;">direction</code>방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">3 ≤ <code style="user-select: auto;">numbers</code>의 길이 ≤ 20</li>
<li style="user-select: auto;"><code style="user-select: auto;">direction</code>은 "left" 와 "right" 둘 중 하나입니다.</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">numbers</th>
<th style="user-select: auto;">direction</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">[1, 2, 3]</td>
<td style="user-select: auto;">"right"</td>
<td style="user-select: auto;">[3, 1, 2]</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">[4, 455, 6, 4, -1, 45, 6]</td>
<td style="user-select: auto;">"left"</td>
<td style="user-select: auto;">[455, 6, 4, -1, 45, 6, 4]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">numbers</code> 가 [1, 2, 3]이고 <code style="user-select: auto;">direction</code>이 "right" 이므로 오른쪽으로 한 칸씩 회전시킨 [3, 1, 2]를 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">numbers</code> 가 [4, 455, 6, 4, -1, 45, 6]이고 <code style="user-select: auto;">direction</code>이 "left" 이므로 왼쪽으로 한 칸씩 회전시킨 [455, 6, 4, -1, 45, 6, 4]를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges