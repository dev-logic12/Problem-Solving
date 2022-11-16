# [level 0] 인덱스 바꾸기 - 120895 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120895) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">문자열 <code style="user-select: auto;">my_string</code>과 정수 <code style="user-select: auto;">num1</code>, <code style="user-select: auto;">num2</code>가 매개변수로 주어질 때, <code style="user-select: auto;">my_string</code>에서 인덱스 <code style="user-select: auto;">num1</code>과 인덱스 <code style="user-select: auto;">num2</code>에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">1 &lt; <code style="user-select: auto;">my_string</code>의 길이 &lt; 100</li>
<li style="user-select: auto;">0 ≤ <code style="user-select: auto;">num1</code>, <code style="user-select: auto;">num2</code> &lt; <code style="user-select: auto;">my_string</code>의 길이</li>
<li style="user-select: auto;"><code style="user-select: auto;">my_string</code>은 소문자로 이루어져 있습니다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">num1</code> ≠ <code style="user-select: auto;">num2</code></li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">my_string</th>
<th style="user-select: auto;">num1</th>
<th style="user-select: auto;">num2</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">"hello"</td>
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">"hlelo"</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">"I love you"</td>
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">6</td>
<td style="user-select: auto;">"I l veoyou"</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"hello"의 1번째 인덱스인 "e"와 2번째 인덱스인 "l"을 바꾸면 "hlelo"입니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"I love you"의 3번째 인덱스 "o"와 " "(공백)을 바꾸면 "I l veoyou"입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges