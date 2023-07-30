<template>
	<div id="app" class="app-all-main" v-loading="vuex_loading">
		<div style="color: #999;font-size: 12px;">
			参与总人数：
			{{userNoForSelect.length + userGet1.length + userGet2.length + userGet3.length + userGet4.length + userGet5.length}}
			,
			暂未中奖 {{userNoForSelect.length}} 人，
			一等奖 {{userGet1.length}} 人，
			二等奖 {{userGet2.length}} 人，
			三等奖 {{userGet3.length}} 人，
			幸运奖 {{userGet4.length}} 人，
			额外奖 {{userGet5.length}} 人。
		</div>
		<div class="main">
			<div class="list">
				<div class="item" v-for="(item,index) in userNoForShow"
					:style="'background-color: ' + (currentNeed.includes(index) ? color2 : color1)">
					{{item.num}}
					<!-- {{index}} -->
				</div>
			</div>
		</div>
		<div class="cenTips">
			<template v-if="allOver">
				所有奖项均已抽出
			</template>
			<template v-else>
				接下来将抽出
				<span style="color: #e54d42;"> {{curSelect.type | rewordFilter}}</span>
				{{curSelect.num}}
				人
			</template>
		</div>
		<div class="btns">
			<el-button class="btn" @click="hadShow = false" v-if="hadShow" type="primary">关闭</el-button>
			<el-button class="btn" @click="contu" v-else-if="centerShow" type="primary">继续</el-button>
			<template v-else>
				<el-button class="btn" @click="start" v-if="flag" type="primary">开始</el-button>
				<el-button class="btn" @click="stop" v-else type="success">停止</el-button>
			</template>
		</div>
		<div class="menus">
			<el-button class="btn" type="primary" @click="getUsers" plain>更新号池</el-button>
			<el-button class="btn" type="success" @click="hadShow = true" plain>中奖名单</el-button>
			<el-button class="btn" type="danger" @click="reset" plain>重置</el-button>
		</div>
		<div :class="'centerShow' + (centerShow ? '' : ' unShow')">
			<div class="box">
				<div class="top">
					恭喜以下号码获得{{curSelect.type | rewordFilter}}
				</div>
				<div class="list">
					<div v-for="(item, index) in currentShow" class="item ce">
						{{item.num}}
					</div>
				</div>
			</div>
		</div>

		<div :class="'hadShow' + (hadShow ? '' : ' unShow')">
			<div class="hadItem" v-if="userGet1.length > 0">
				<div class="itemTitle">一等奖</div>
				<div class="item listItem" v-for="item in userGet1">{{item.num}}</div>
			</div>
			<div class="hadItem" v-if="userGet2.length > 0">
				<div class="itemTitle">二等奖</div>
				<div class="item listItem" v-for="item in userGet2">{{item.num}}</div>
			</div>
			<div class="hadItem" v-if="userGet3.length > 0">
				<div class="itemTitle">三等奖</div>
				<div class="item listItem" v-for="item in userGet3">{{item.num}}</div>
			</div>
			<div class="hadItem" v-if="userGet4.length > 0">
				<div class="itemTitle">幸运奖</div>
				<div class="item listItem" v-for="item in userGet4">{{item.num}}</div>
			</div>
			<div class="hadItem" v-if="userGet5.length > 0">
				<div class="itemTitle">额外奖</div>
				<div class="item listItem" v-for="item in userGet5">{{item.num}}</div>
			</div>
			<div class="noneData" v-if="userGet1.length < 1 && userGet2.length < 1 && userGet3.length < 1 && userGet4.length < 1 && userGet5.length < 1">暂无</div>
		</div>

	</div>
</template>
<script>
	import _ from 'lodash';
	import {
		getAllUser,
		setUserStatus,
		resetAllStatus
	} from '@/api/api.js'
	export default {
		name: "App",
		data() {
			return {
				userNoForShow: [],
				userNoForSelect: [],
				userGet1: [],
				userGet2: [],
				userGet3: [],
				userGet4: [],
				userGet5: [],
				color1: '#1cbbb4',
				color2: '#e03997',
				timer: null,
				currentNeed: [],
				timerCur: null,
				flag: true,
				frKey: null,
				curSelect: {
					num: 10,
					type: 1
				},
				centerShow: false,
				currentShow: [],
				allOver: false,
				hadShow: false
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
					this.userGet5 = [];
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
						} else if (item.reword == 5) {
							this.userGet5.push(item);
						}
					}
					this.userNoForSelect = JSON.parse(JSON.stringify(userNo));
					this.userNoDe();
					this.getNext();
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
				this.userNoForShow = _.shuffle(userNTmp);
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
				let cu = JSON.parse(JSON.stringify(this.userNoForSelect));
				this.currentShow = _.shuffle(cu).slice(0, this.curSelect.num);
				let data = {
					frKey: this.frKey,
					reword: this.curSelect.type,
					userIds: this.currentShow.map(item => {
						return item.id;
					}).join(',')
				}
				setUserStatus(data).then(res => {
					this.centerShow = true;
				})
			},
			getQueryString(name) {
				var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
				var r = window.location.search.substr(1).match(reg);
				if (r != null) return unescape(r[2]);
				return null;
			},
			contu() {
				this.centerShow = false;
				this.currentShow = [];
				this.getUsers();
			},
			getNext() {
				this.allOver = false;
				if (this.userGet3.length < 10) {
					this.curSelect = {
						num: 10 - this.userGet3.length,
						type: 3
					}
				} else if (this.userGet2.length < 5) {
					this.curSelect = {
						num: 5 - this.userGet2.length,
						type: 2
					}
				} else if (this.userGet1.length < 1) {
					this.curSelect = {
						num: 1,
						type: 1
					}
				} else if (this.userGet4.length < 3) {
					this.curSelect = {
						num: 3 - this.userGet4.length,
						type: 4
					}
				} else {
					this.curSelect = {
						num: 1,
						type: 5
					}
					this.allOver = true;
				}
			},
			reset() {
				this.$confirm('此操作将清空现有所有抽奖，确认吗?', '提示', {
					confirmButtonText: '确定',
					cancelButtonText: '取消',
					type: 'warning'
				}).then(() => {
					resetAllStatus({
						frKey: this.frKey
					}).then(res => {
						this.$message({
							message: res.msg,
							type: 'success'
						});
						this.getUsers();
					})
				}).catch(() => {});
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
			height: 86px;
			transition: all .3s;
		}

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
			}
		}

		.cenTips {
			text-align: center;
			font-size: 60px;
			font-weight: bold;
			color: #0081ff;
		}

		.btns {
			position: absolute;
			bottom: 80px;
			left: 0;
			right: 0;
			display: flex;
			justify-content: center;
			margin-top: 200px;

			.btn {
				width: 200px;
				height: 100px;
				font-size: 40px;
				z-index: 10;
			}
		}

		.menus {
			position: absolute;
			right: 80px;
			bottom: 100px;
			display: block;
			z-index: 3;
		}

		.centerShow {
			position: absolute;
			z-index: 5;
			left: 0;
			right: 0;
			top: 0;
			bottom: 0;
			background-color: rgba(255, 255, 255, .9);
			display: flex;
			justify-content: center;
			overflow: hidden;
			transition: all .3s;

			.box {
				.top {
					text-align: center;
					color: #e54d42;
					font-size: 80px;
					font-weight: bold;
					margin: 80px 0;
				}

				.list {
					display: flex;
					flex-wrap: wrap;
					justify-content: center;
					width: 300*5px;

					.ce {
						background-color: #e54d42;
						margin: 20px;
						width: 260px;
						height: 130px;
						font-size: 68px;
					}
				}

				.bottom {
					margin-top: 340px;
					text-align: center;
				}
			}
		}

		.hadShow {
			position: absolute;
			z-index: 5;
			left: 0;
			right: 0;
			top: 0;
			bottom: 0;
			background-color: rgba(255, 255, 255, .9);
			transition: all .3s;
			padding: 0 120px;
			overflow: hidden;

			.hadItem {
				display: flex;
				justify-content: left;
				align-items: center;
				flex-wrap: wrap;
				margin: 60px 0;

				.itemTitle {
					text-align: center;
					color: #0081ff;
					font-weight: bold;
					font-size: 50px;
					margin-right: 40px;
				}

				.listItem {
					background-color: #e54d42;
					margin: 10px;
					width: 120px;
					height: 80px;
					font-size: 39px;
				}
			}
			
			.noneData {
				text-align: center;
				color: #666;
				font-size: 120px;
			}
		}

		.unShow {
			left: 50%;
			right: 50%;
			top: 50%;
			bottom: 50%;
		}
	}
</style>