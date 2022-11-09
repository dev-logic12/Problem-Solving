# [level 0] 2차원으로 만들기 - 120842 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120842) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">정수 배열 <code style="user-select: auto;">num_list</code>와 정수&nbsp;<code style="user-select: auto;">n</code>이 매개변수로 주어집니다. <code style="user-select: auto;">num_list</code>를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.</p>

<p style="user-select: auto;"><code style="user-select: auto;">num_list</code>가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 <code style="user-select: auto;">n</code>이 2이므로 <code style="user-select: auto;">num_list</code>를 2 * 4 배열로 다음과 같이 변경합니다. 2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.</p>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">num_list</th>
<th style="user-select: auto;">n</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">[1, 2, 3, 4, 5, 6, 7, 8]</td>
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">[[1, 2], [3, 4], [5, 6], [7, 8]]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">num_list</code>의 길이는&nbsp;<code style="user-select: auto;">n</code>의 배 수개입니다.</li>
<li style="user-select: auto;">0 ≤ <code style="user-select: auto;">num_list</code>의 길이 ≤ 150</li>
<li style="user-select: auto;">2 ≤ <code style="user-select: auto;">n</code> &lt; <code style="user-select: auto;">num_list</code>의 길이</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">num_list</th>
<th style="user-select: auto;">n</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">[1, 2, 3, 4, 5, 6, 7, 8]</td>
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">[[1, 2], [3, 4], [5, 6], [7, 8]]</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">[100, 95, 2, 4, 5, 6, 18, 33, 948]</td>
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">[[100, 95, 2], [4, 5, 6], [18, 33, 948]]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">num_list</code>가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 <code style="user-select: auto;">n</code>이 2이므로 2 * 4 배열로 변경한 [[1, 2], [3, 4], [5, 6], [7, 8]] 을 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">num_list</code>가 [100, 95, 2, 4, 5, 6, 18, 33, 948] 로 길이가 9이고 <code style="user-select: auto;">n</code>이 3이므로 3 * 3 배열로 변경한 [[100, 95, 2], [4, 5, 6], [18, 33, 948]] 을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges