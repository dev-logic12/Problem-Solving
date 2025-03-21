# [level 0] 특별한 이차원 배열 2 - 181831 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181831?language=python3) 

### 성능 요약

메모리: 10.5 MB, 시간: 0.27 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 03월 21일 11:25:51

### 문제 설명

<p style="user-select: auto !important;">n × n 크기의 이차원 배열 <code style="user-select: auto !important;">arr</code>이 매개변수로 주어질 때, <code style="user-select: auto !important;">arr</code>이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">0 ≤ i, j &lt; n인 정수 i, j에 대하여 <code style="user-select: auto !important;">arr[i][j]</code> = <code style="user-select: auto !important;">arr[j][i]</code></li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr</code>의 길이 = <code style="user-select: auto !important;">arr</code>의 원소의 길이 ≤ 100</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr</code>의 원소의 원소 ≤ 1,000</li>
<li style="user-select: auto !important;">모든 <code style="user-select: auto !important;">arr</code>의 원소의 길이는 같습니다.</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">arr</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[[5, 192, 33], [192, 72, 95], [33, 95, 999]]</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]</td>
<td style="user-select: auto !important;">0</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 1번에서 문제의 조건이 잘 보이도록 표를 만들면 다음과 같습니다.</li>
</ul>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">i</th>
<th style="user-select: auto !important;">j</th>
<th style="user-select: auto !important;">arr[i][j]</th>
<th style="user-select: auto !important;">arr[j][i]</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">5</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">192</td>
<td style="user-select: auto !important;">192</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">33</td>
<td style="user-select: auto !important;">33</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">192</td>
<td style="user-select: auto !important;">192</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">72</td>
<td style="user-select: auto !important;">72</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">95</td>
<td style="user-select: auto !important;">95</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">0</td>
<td style="user-select: auto !important;">33</td>
<td style="user-select: auto !important;">33</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">95</td>
<td style="user-select: auto !important;">95</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">999</td>
<td style="user-select: auto !important;">999</td>
</tr>
</tbody>
      </table><div class="highlight" style="user-select: auto !important;"><pre class="codehilite" style="user-select: auto !important;"><code style="user-select: auto !important;">조건을 만족하므로 1을 return 합니다.
</code></pre></div>
<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 2번의 <code style="user-select: auto !important;">arr</code>에서 <code style="user-select: auto !important;">arr[0][1]</code> = 498 ≠ 63 = <code style="user-select: auto !important;">arr[1][0]</code>이므로 조건을 만족하지 않습니다. 따라서 0을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges