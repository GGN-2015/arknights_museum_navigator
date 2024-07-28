#include <cassert>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <tuple>
using namespace std;

const int maxn = 1024, maxhammer = 5;
int maze[maxn][maxn];
int vis[maxn][maxn][maxhammer];
int dis[maxn][maxn][maxhammer];
tuple<int, int, int> pre[maxn][maxn][maxhammer];

const int dx[] = {1, 0,-1, 0};
const int dy[] = {0,-1, 0, 1};

int main() {
    int n, m; scanf("%d%d", &n, &m);
    int ham_cnt; scanf("%d", &ham_cnt);
    for(int i = 0; i <= n + 1; i += 1) {
        for(int j = 0; j <= m + 1; j += 1) {
            maze[i][j] = -1; // -1: dead wall
        }
    }
    for(int i = 1; i <= n; i += 1) {
        for(int j = 1; j <= m; j += 1) {
            scanf("%d", &maze[i][j]); // 0: path, 1: wall
        }
    }
    queue<tuple<int, int, int>> q;
    q.push(make_tuple(1, 1, ham_cnt));
    vis[1][1][ham_cnt] = 1;
    while(!q.empty()) {
        auto [x, y, cnt] = q.front(); q.pop(); 
	// printf("x = %d, y = %d, cnt = %d\n", x, y, cnt);
	for(int d = 0; d <= 3; d += 1) {
            int nx = x + dx[d];
	    int ny = y + dy[d];
	    if(maze[nx][ny] == -1) continue;
            if(maze[nx][ny] == 0) {
	        if(!vis[nx][ny][cnt]) {
		    vis[nx][ny][cnt] = 1;
		    dis[nx][ny][cnt] = dis[x][y][cnt] + 1;
		    q.push(make_tuple(nx, ny, cnt));
		    pre[nx][ny][cnt] = make_tuple(x, y, cnt);
		}
	    }
	    if(maze[nx][ny] == 1) {
                if(cnt > 0) {
                    int ncnt = cnt - 1;
		    if(!vis[nx][ny][ncnt]) {
                        vis[nx][ny][ncnt] = 1;
			dis[nx][ny][ncnt] = dis[x][y][cnt] + 1;
			q.push(make_tuple(nx, ny, ncnt));
			pre[nx][ny][ncnt] = make_tuple(x, y, cnt);
		    }
		}
	    }
	}
    }
    int dis_now = 0x7f7f7f7f;
    int cnt_now = -1;
    for(int i = 0; i <= ham_cnt; i += 1) {
	if(vis[n][m][i]) {
            if(dis_now > dis[n][m][i]) {
	        dis_now = dis[n][m][i];
		cnt_now = i;
	    }
	}
    }
    assert(cnt_now != -1);
    int nx = n, ny = m, ncnt = cnt_now;
    while(true) {
	printf("%d %d\n", nx, ny);	    
	if(nx == 1 && ny == 1) break;
	auto [x, y, c] = pre[nx][ny][ncnt];
	nx = x;
	ny = y;
	ncnt = c;
    }
    return 0;
}
