<template>
	<div id="app" class="app-all-main">
		<div class="main">
			<div class="list">
				<div class="item" v-for="(item,index) in userNo"
					:style="'background-color: ' + (currentNeed.includes(index) ? color2 : color1)">
					{{item.num}}
				</div>
			</div>
		</div>
		<div class="btns">
			<el-button class="btn" @click="start" v-if="flag" type="primary">开始</el-button>
			<el-button class="btn" @click="stop" v-else type="success">停止</el-button>
		</div>
	</div>
</template>
<script>
	import _ from 'lodash';
	import {
		getAllUser,
		setUserStatus
	} from '@/api/api.js'
	export default {
		name: "App",
		data() {
			return {
				userNo: [],
				userNoForSelect: [],
				userGet1: [],
				userGet2: [],
				userGet3: [],
				userGet4: [],
				color1: '#1cbbb4',
				color2: '#9c26b0',
				timer: null,
				currentNeed: [],
				timerCur: null,
				flag: true,
				frKey: null
			};
		},
		created() {
			this.frKey = this.getQueryString('frKey');
			this.getUsers();
			this.curStart();
		},
		methods: {
			getUsers() {
				getAllUser({
					frKey: this.frKey
				}).then(res => {
					let userNo = [];
					this.userGet1 = [];
					this.userGet2 = [];
					this.userGet3 = [];
					this.userGet4 = [];
					for (let i in res.data) {
						let item = res.data[i];
						if (item.status == 0) {
							userNo.push(item);
						} else if (item.reword == 1) {
							this.userGet1.push(item);
						} else if (item.reword == 2) {
							this.userGet2.push(item);
						} else if (item.reword == 3) {
							this.userGet3.push(item);
						} else if (item.reword == 4) {
							this.userGet4.push(item);
						}
					}
					this.userNoForSelect = JSON.parse(JSON.stringify(userNo));
					this.userNoDe();
				})
			},
			getCurrent() {
				let needs = [];
				needs.push(this.get2023());
				needs.push(this.get0806());
				needs.push(this.gethlqh());
				let tm = Date.parse(new Date()) / 1000;
				this.currentNeed = needs[tm % 3];
			},
			curStart() {
				let that = this;
				that.getCurrent();
				this.timerCur = setInterval(function() {
					that.getCurrent();
				}, 4000);
			},
			curStop() {
				clearInterval(this.timerCur);
				this.timerCur = null;
			},
			get2023() {
				let need = [18, 19, 20, 37, 54, 53, 52, 69, 86, 87, 88]; // 2
				need = need.concat([22, 23, 24, 41, 58, 75, 92, 91, 90, 73, 56, 39]); // 0
				need = need.concat([26, 27, 28, 45, 62, 61, 60, 77, 94, 95, 96]); // 2
				need = need.concat([30, 31, 32, 49, 66, 65, 64, 83, 100, 99, 98]); // 3
				return need;
			},
			get0806() {
				let need = [18, 19, 20, 37, 54, 71, 88, 87, 86, 69, 52, 35]; // 0
				need = need.concat([22, 23, 24, 41, 58, 75, 92, 91, 90, 73, 56, 39, 57]); // 8
				need = need.concat([26, 27, 28, 45, 62, 79, 60, 77, 94, 95, 96, 43]); // 0
				need = need.concat([30, 31, 32, 47, 66, 65, 64, 83, 100, 99, 98, 81]); // 6
				return need;
			},
			gethlqh() {
				let need = [18, 35, 20, 37, 54, 53, 52, 69, 86, 71, 88]; // H
				need = need.concat([22, 92, 91, 90, 73, 56, 39]); // L
				need = need.concat([26, 27, 28, 45, 62, 61, 60, 43, 79, 96]); // q
				need = need.concat([30, 47, 32, 49, 66, 65, 64, 83, 100, 81, 98]); // H
				return need;
			},
			// 未中奖数据处理
			userNoDe() {
				let userNTmp = JSON.parse(JSON.stringify(this.userNoForSelect));
				let i = 0;
				while (userNTmp.length < 17 * 7) {
					userNTmp.push(JSON.parse(JSON.stringify(userNTmp[i])));
					i = i + 1;
				}
				this.userNo = _.shuffle(userNTmp);
			},
			start() {
				this.flag = !this.flag;
				let that = this;
				that.timer = setInterval(function() {
					that.userNoDe();
				}, 20);
			},
			stop() {
				this.flag = !this.flag;
				clearInterval(this.timer);
				this.timer = null;
			},
			getQueryString(name) {
			var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
			var r = window.location.search.substr(1).match(reg);
			if (r != null) return unescape(r[2]);
			return null;
			}
		}
	};
</script>
<style lang="scss">
	body {
		margin: 0;
	}

	#app {
		width: 100vw;
		height: 100vh;
		overflow: hidden;
		background-color: rgba(229, 77, 66, .1);


		.main {
			margin: 30px;
			padding: 30px 60px;
			border-radius: 10px;
			display: flex;
			align-items: center;
			justify-content: center;
			z-index: 1;

			.list {
				display: flex;
				flex-wrap: wrap;
				width: 90*17px;

				.item {
					color: #FFFFFF;
					font-size: 18px;
					margin: 2px;
					border-radius: 2px;
					font-weight: bold;
					display: flex;
					align-items: center;
					justify-content: center;
					width: 86px;
					height: 68px;
				}
			}
		}
		
		.btns {
			display: flex;
			justify-content: center;
			margin-top: 200px;
			z-index: 10;
			
			.btn {
				width: 200px;
				height: 100px;
				font-size: 40px;
			}
		}
	}
</style>