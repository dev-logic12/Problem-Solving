# [level 0] 소인수분해 - 120852 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120852?language=python3) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 자연수 <code style="user-select: auto;">n</code>이 매개변수로 주어질 때 <code style="user-select: auto;">n</code>의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">2 ≤ <code style="user-select: auto;">n</code> ≤ 10,000</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">n</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">12</td>
<td style="user-select: auto;">[2, 3]</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">17</td>
<td style="user-select: auto;">[17]</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">420</td>
<td style="user-select: auto;">[2, 3, 5, 7]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">12를 소인수분해하면 2 * 2 * 3 입니다. 따라서 [2, 3]을 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">17은 소수입니다. 따라서 [17]을 return 해야 합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #3</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">420을 소인수분해하면 2 * 2 * 3 * 5 * 7 입니다. 따라서 [2, 3, 5, 7]을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges