# [level 0] 숫자 찾기 - 120904 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120904) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">정수 <code style="user-select: auto;">num</code>과 <code style="user-select: auto;">k</code>가 매개변수로 주어질 때, <code style="user-select: auto;">num</code>을 이루는 숫자 중에 <code style="user-select: auto;">k</code>가 있으면 <code style="user-select: auto;">num</code>의  그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">0 &lt; <code style="user-select: auto;">num</code> &lt; 1,000,000</li>
<li style="user-select: auto;">0 ≤ <code style="user-select: auto;">k</code> &lt; 10</li>
<li style="user-select: auto;"><code style="user-select: auto;">num</code>에 <code style="user-select: auto;">k</code>가 여러 개 있으면 가장 처음 나타나는 자리를 return 합니다.</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">num</th>
<th style="user-select: auto;">k</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">29183</td>
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">3</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">232443</td>
<td style="user-select: auto;">4</td>
<td style="user-select: auto;">4</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">123456</td>
<td style="user-select: auto;">7</td>
<td style="user-select: auto;">-1</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">29183에서 1은 3번째에 있습니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">232443에서 4는 4번째에 처음 등장합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #3</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">123456에 7은 없으므로 -1을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges