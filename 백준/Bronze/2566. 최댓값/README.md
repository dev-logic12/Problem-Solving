# [Bronze III] 최댓값 - 2566 

[문제 링크](https://www.acmicpc.net/problem/2566) 

### 성능 요약

메모리: 30616 KB, 시간: 36 ms

### 분류

구현(implementation)

### 문제 설명

<p style="user-select: auto;"><그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.</p>

<p style="user-select: auto;">예를 들어, 다음과 같이 81개의 수가 주어지면</p>

<table class="table table-bordered td-center th-center table-center-40" style="user-select: auto;">
	<tbody style="user-select: auto;">
		<tr style="user-select: auto;">
			<th style="user-select: auto;"> </th>
			<th style="user-select: auto;">1열</th>
			<th style="user-select: auto;">2열</th>
			<th style="user-select: auto;">3열</th>
			<th style="user-select: auto;">4열</th>
			<th style="user-select: auto;">5열</th>
			<th style="user-select: auto;">6열</th>
			<th style="user-select: auto;">7열</th>
			<th style="user-select: auto;">8열</th>
			<th style="user-select: auto;">9열</th>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">1행</th>
			<td style="user-select: auto;">3</td>
			<td style="user-select: auto;">23</td>
			<td style="user-select: auto;">85</td>
			<td style="user-select: auto;">34</td>
			<td style="user-select: auto;">17</td>
			<td style="user-select: auto;">74</td>
			<td style="user-select: auto;">25</td>
			<td style="user-select: auto;">52</td>
			<td style="user-select: auto;">65</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">2행</th>
			<td style="user-select: auto;">10</td>
			<td style="user-select: auto;">7</td>
			<td style="user-select: auto;">39</td>
			<td style="user-select: auto;">42</td>
			<td style="user-select: auto;">88</td>
			<td style="user-select: auto;">52</td>
			<td style="user-select: auto;">14</td>
			<td style="user-select: auto;">72</td>
			<td style="user-select: auto;">63</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">3행</th>
			<td style="user-select: auto;">87</td>
			<td style="user-select: auto;">42</td>
			<td style="user-select: auto;">18</td>
			<td style="user-select: auto;">78</td>
			<td style="user-select: auto;">53</td>
			<td style="user-select: auto;">45</td>
			<td style="user-select: auto;">18</td>
			<td style="user-select: auto;">84</td>
			<td style="user-select: auto;">53</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">4행</th>
			<td style="user-select: auto;">34</td>
			<td style="user-select: auto;">28</td>
			<td style="user-select: auto;">64</td>
			<td style="user-select: auto;">85</td>
			<td style="user-select: auto;">12</td>
			<td style="user-select: auto;">16</td>
			<td style="user-select: auto;">75</td>
			<td style="user-select: auto;">36</td>
			<td style="user-select: auto;">55</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">5행</th>
			<td style="user-select: auto;">21</td>
			<td style="user-select: auto;">77</td>
			<td style="user-select: auto;">45</td>
			<td style="user-select: auto;">35</td>
			<td style="user-select: auto;">28</td>
			<td style="user-select: auto;">75</td>
			<td style="user-select: auto;">90</td>
			<td style="user-select: auto;">76</td>
			<td style="user-select: auto;">1</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">6행</th>
			<td style="user-select: auto;">25</td>
			<td style="user-select: auto;">87</td>
			<td style="user-select: auto;">65</td>
			<td style="user-select: auto;">15</td>
			<td style="user-select: auto;">28</td>
			<td style="user-select: auto;">11</td>
			<td style="user-select: auto;">37</td>
			<td style="user-select: auto;">28</td>
			<td style="user-select: auto;">74</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">7행</th>
			<td style="user-select: auto;">65</td>
			<td style="user-select: auto;">27</td>
			<td style="user-select: auto;">75</td>
			<td style="user-select: auto;">41</td>
			<td style="user-select: auto;">7</td>
			<td style="user-select: auto;">89</td>
			<td style="user-select: auto;">78</td>
			<td style="user-select: auto;">64</td>
			<td style="user-select: auto;">39</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">8행</th>
			<td style="user-select: auto;">47</td>
			<td style="user-select: auto;">47</td>
			<td style="user-select: auto;">70</td>
			<td style="user-select: auto;">45</td>
			<td style="user-select: auto;">23</td>
			<td style="user-select: auto;">65</td>
			<td style="user-select: auto;">3</td>
			<td style="user-select: auto;">41</td>
			<td style="user-select: auto;">44</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">9행</th>
			<td style="user-select: auto;">87</td>
			<td style="user-select: auto;">13</td>
			<td style="user-select: auto;">82</td>
			<td style="user-select: auto;">38</td>
			<td style="user-select: auto;">31</td>
			<td style="user-select: auto;">12</td>
			<td style="user-select: auto;">29</td>
			<td style="user-select: auto;">29</td>
			<td style="user-select: auto;">80</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto;">이들 중 최댓값은 90이고, 이 값은 5행 7열에 위치한다.</p>

### 입력 

 <p style="user-select: auto;">첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 작은 자연수 또는 0이다.</p>

### 출력 

 <p style="user-select: auto;">첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다. 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.</p>

