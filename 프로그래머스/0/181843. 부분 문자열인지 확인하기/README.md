# [level 0] 부분 문자열인지 확인하기 - 181843 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181843) 

### 성능 요약

메모리: 9.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 04월 11일 12:08:17

### 문제 설명

<p style="user-select: auto !important;">부분 문자열이란 문자열에서 연속된 일부분에 해당하는 문자열을 의미합니다. 예를 들어, 문자열 "ana", "ban", "anana", "banana", "n"는 모두 문자열 "banana"의 부분 문자열이지만, "aaa", "bnana", "wxyz"는 모두 "banana"의 부분 문자열이 아닙니다.</p>

<p style="user-select: auto !important;">문자열 <code style="user-select: auto !important;">my_string</code>과 <code style="user-select: auto !important;">target</code>이 매개변수로 주어질 때, <code style="user-select: auto !important;">target</code>이 문자열 <code style="user-select: auto !important;">my_string</code>의 부분 문자열이라면 1을, 아니라면 0을 return 하는 solution 함수를 작성해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">my_string</code>의 길이 ≤ 100</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">my_string</code>은 영소문자로만 이루어져 있습니다.</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">target</code>의 길이 ≤ 100</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">target</code>은 영소문자로만 이루어져 있습니다.</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">my_string</th>
<th style="user-select: auto !important;">target</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">"banana"</td>
<td style="user-select: auto !important;">"ana"</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">"banana"</td>
<td style="user-select: auto !important;">"wxyz"</td>
<td style="user-select: auto !important;">0</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">문제 설명과 같습니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">문제 설명과 같습니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges