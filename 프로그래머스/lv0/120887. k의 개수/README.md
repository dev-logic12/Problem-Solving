# [level 0] k의 개수 - 120887 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120887) 

### 성능 요약

메모리: 11.1 MB, 시간: 2.53 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 <code style="user-select: auto;">i</code>, <code style="user-select: auto;">j</code>, <code style="user-select: auto;">k</code>가 매개변수로 주어질 때, <code style="user-select: auto;">i</code>부터 <code style="user-select: auto;">j</code>까지 <code style="user-select: auto;">k</code>가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">i</code> &lt; <code style="user-select: auto;">j</code> ≤ 100,000</li>
<li style="user-select: auto;">0 ≤ <code style="user-select: auto;">k</code> ≤ 9</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">i</th>
<th style="user-select: auto;">j</th>
<th style="user-select: auto;">k</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">13</td>
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">6</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">10</td>
<td style="user-select: auto;">50</td>
<td style="user-select: auto;">5</td>
<td style="user-select: auto;">5</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">10</td>
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">0</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">본문과 동일합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">10부터 50까지 5는 15, 25, 35, 45, 50 총 5번 등장합니다. 따라서 5를 return 합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #3</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">3부터 10까지 2는 한 번도 등장하지 않으므로 0을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges