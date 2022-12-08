# [Bronze II] 카드놀이 - 2511 

[문제 링크](https://www.acmicpc.net/problem/2511) 

### 성능 요약

메모리: 30616 KB, 시간: 36 ms

### 분류

구현(implementation)

### 문제 설명

<p style="user-select: auto;">0부터 9까지의 숫자가 표시된 카드를 가지고 두 사람 A와 B가 게임을 한다. A와 B에게는 각각 0에서 9까지의 숫자가 하나씩 표시된 10장의 카드뭉치가 주어진다. 두 사람은 카드를 임의의 순서로 섞은 후 숫자가 보이지 않게 일렬로 늘어  놓고 게임을 시작한다. 단, 게임 도중 카드의 순서를 바꿀 수는 없다.</p>

<p style="user-select: auto;">A와 B 각각이 늘어놓은 카드를 뒤집어서 표시된 숫자를 확인하는 것을 한 라운드라고 한다. 게임은 첫 번째 놓인 카드부터 시작하여 순서대로 10번의 라운드로 진행된다. 각 라운드에서는 공개된 숫자가 더 큰 사람이 승자가 된다. 승자에게는 승점 3점이 주어지고 패자에게는 승점이 주어지지 않는다. 만약 공개된 두 숫자가 같아서 비기게 되면, A, B 모두에게 승점 1점이 주어진다. </p>

<p style="user-select: auto;">10번의 라운드가 모두 진행된 후, 총 승점이 큰 사람이 게임의 승자가 된다. 만약, A와 B의 총 승점이 같은 경우에는, 제일 마지막에 이긴 사람을 게임의 승자로 정한다. 그래도 승부가 나지 않는 경우는 모든 라운드에서 비기는 경우뿐이고 이 경우에 두 사람은 비겼다고 한다.</p>

<p style="user-select: auto;">예를 들어, 다음 표에서 3번째 줄은 각 라운드의 승자를 표시하고 있다. 표에서 D는 무승부를 나타낸다. 이 경우에 A의 총 승점은 16점이고, B는 13점이어서, A가 게임의 승자가 된다. </p>

<table class="table table-bordered td-center th-center table-center-50" style="user-select: auto;">
	<thead style="user-select: auto;">
		<tr style="user-select: auto;">
			<th style="user-select: auto;">라운드</th>
			<th style="user-select: auto;">1</th>
			<th style="user-select: auto;">2</th>
			<th style="user-select: auto;">3</th>
			<th style="user-select: auto;">4</th>
			<th style="user-select: auto;">5</th>
			<th style="user-select: auto;">6</th>
			<th style="user-select: auto;">7</th>
			<th style="user-select: auto;">8</th>
			<th style="user-select: auto;">9</th>
			<th style="user-select: auto;">10</th>
		</tr>
	</thead>
	<tbody style="user-select: auto;">
		<tr style="user-select: auto;">
			<th style="user-select: auto;">A</th>
			<td style="user-select: auto;">4</td>
			<td style="user-select: auto;">5</td>
			<td style="user-select: auto;">6</td>
			<td style="user-select: auto;">7</td>
			<td style="user-select: auto;">0</td>
			<td style="user-select: auto;">1</td>
			<td style="user-select: auto;">2</td>
			<td style="user-select: auto;">3</td>
			<td style="user-select: auto;">9</td>
			<td style="user-select: auto;">8</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">B</th>
			<td style="user-select: auto;">1</td>
			<td style="user-select: auto;">2</td>
			<td style="user-select: auto;">3</td>
			<td style="user-select: auto;">4</td>
			<td style="user-select: auto;">5</td>
			<td style="user-select: auto;">6</td>
			<td style="user-select: auto;">7</td>
			<td style="user-select: auto;">8</td>
			<td style="user-select: auto;">9</td>
			<td style="user-select: auto;">0</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">승</th>
			<td style="user-select: auto;">A</td>
			<td style="user-select: auto;">A</td>
			<td style="user-select: auto;">A</td>
			<td style="user-select: auto;">A</td>
			<td style="user-select: auto;">B</td>
			<td style="user-select: auto;">B</td>
			<td style="user-select: auto;">B</td>
			<td style="user-select: auto;">B</td>
			<td style="user-select: auto;">D</td>
			<td style="user-select: auto;">A</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto;">아래 표의 경우에는 A와 B의 총 승점은 13점으로 같다. 마지막으로 승부가 난 라운드는 7번째 라운드이고, 이 라운드의 승자인 B가 게임의 승자가 된다. </p>

<table class="table table-bordered td-center th-center table-center-50" style="user-select: auto;">
	<thead style="user-select: auto;">
		<tr style="user-select: auto;">
			<th style="user-select: auto;">라운드</th>
			<th style="user-select: auto;">1</th>
			<th style="user-select: auto;">2</th>
			<th style="user-select: auto;">3</th>
			<th style="user-select: auto;">4</th>
			<th style="user-select: auto;">5</th>
			<th style="user-select: auto;">6</th>
			<th style="user-select: auto;">7</th>
			<th style="user-select: auto;">8</th>
			<th style="user-select: auto;">9</th>
			<th style="user-select: auto;">10</th>
		</tr>
	</thead>
	<tbody style="user-select: auto;">
		<tr style="user-select: auto;">
			<th style="user-select: auto;">A</th>
			<td style="user-select: auto;">9</td>
			<td style="user-select: auto;">1</td>
			<td style="user-select: auto;">7</td>
			<td style="user-select: auto;">2</td>
			<td style="user-select: auto;">6</td>
			<td style="user-select: auto;">3</td>
			<td style="user-select: auto;">0</td>
			<td style="user-select: auto;">4</td>
			<td style="user-select: auto;">8</td>
			<td style="user-select: auto;">5</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">B</th>
			<td style="user-select: auto;">6</td>
			<td style="user-select: auto;">3</td>
			<td style="user-select: auto;">9</td>
			<td style="user-select: auto;">2</td>
			<td style="user-select: auto;">1</td>
			<td style="user-select: auto;">0</td>
			<td style="user-select: auto;">7</td>
			<td style="user-select: auto;">4</td>
			<td style="user-select: auto;">8</td>
			<td style="user-select: auto;">5</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">승</th>
			<td style="user-select: auto;">A</td>
			<td style="user-select: auto;">B</td>
			<td style="user-select: auto;">B</td>
			<td style="user-select: auto;">D</td>
			<td style="user-select: auto;">A</td>
			<td style="user-select: auto;">A</td>
			<td style="user-select: auto;">B</td>
			<td style="user-select: auto;">D</td>
			<td style="user-select: auto;">D</td>
			<td style="user-select: auto;">D</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto;">A와 B가 늘어놓은 카드의 숫자가 순서대로 주어질 때, 게임의 승자가 A인지 B인지, 또는 비겼는지 결정하는 프로그램을 작성하시오.</p>

### 입력 

 <p style="user-select: auto;">입력 파일은 두 개의 줄로 이루어진다. 첫 번째 줄에는 A가 늘어놓은 카드의 숫자들이 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 B가 늘어놓은 카드의 숫자들이 빈칸을 사이에 두고 순서대로 주어진다. </p>

### 출력 

 <p style="user-select: auto;">첫 번째 줄에는 게임이 끝난 후, A와 B가 받은 총 승점을 순서대로 빈칸을 사이에 두고 출력한다. 두 번째 줄에는 이긴 사람이 A인지 B인지 결정해서, 이긴 사람을 문자 A 또는 B로 출력한다. 만약 비기는 경우에는 문자 D를 출력한다. </p>

