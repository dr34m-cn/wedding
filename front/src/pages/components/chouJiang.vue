<template>
	<view class="chouJiang">
		<view class="showBack" v-if="show" @click="close"></view>
		<view :class="'box ' + (show ? 'show' : 'hide')">
			<template v-if="show">
				<view class="topClose">
					<u-icon class="close" name="close" color="#FFFFFF" size="26" @click="close"></u-icon>
				</view>
				<view class="content">
					<view class="had" v-if="vuex_hadGetCj">
						<view :class="vuex_cjData == null ? 'getCj' : 'hadCj'">
							<button class="getBtn" v-if="vuex_cjData == null" @click="openCj" :disabled="openLoading">
								<template v-if="openLoading">
									<u-loading-icon size="50"></u-loading-icon>
								</template>
								<template v-else>
									開
								</template>
							</button>
							<view class="numBox" v-else>
								<view class="numTip">您的抽奖号为{{vuex_cjData.status == 1 ? '：'+vuex_cjData.num : ''}}</view>
								<view class="num reword" v-if="vuex_cjData.status == 1">{{vuex_cjData.reword | rewordFilter}}</view>
								<view class="num" v-else>{{vuex_cjData.num}}</view>
								<view class="status">
									状态：
									<span :class="'sts' + vuex_cjData.status">
										{{vuex_cjData.status | statusFilter}}
									</span>
									<view v-if="openLoading" style="padding-left: 18rpx;">
										<u-loading-icon color="#999999"></u-loading-icon>
									</view>
								</view>
							</view>
						</view>
					</view>
					<view class="hadnot" v-else>
						<view class="text">
							请扫描婚礼现场抽奖码<br>获取抽奖资格
						</view>
						<view class="tipBox">
							<button class="tip" size="mini" @click="openCj" :disabled="openLoading">
								<template v-if="openLoading">
									<u-loading-icon size="20"></u-loading-icon>
								</template>
								<template v-else>
									已扫过？点击查询
								</template>
							</button>
						</view>
					</view>
				</view>
			</template>
			<template v-else>
				<view class="red" @click="open">
					<view class="redBox">
						<u-icon name="red-packet-fill" color="#FFFFFF" size="36"></u-icon>
						<view class="redText">抽奖</view>
					</view>
				</view>
			</template>
		</view>
	</view>
</template>

<script>
	import {
		getByJsCode,
		getByOpenId
	} from '@/api/api.js';
	export default {
		name: 'chouJiang',
		data() {
			return {
				show: false,
				openLoading: false,
				timer: null
			}
		},
		methods: {
			open() {
				this.show = true;
				this.refresh();
			},
			close() {
				this.show = false;
				if (this.timer) {
					clearTimeout(this.timer);
				}
			},
			// 开奖方法
			openCj() {
				let that = this;
				this.openLoading = true;
				if (that.vuex_cjData == null) {
					wx.login({
						success(res) {
							if (res.code) {
								getByJsCode({
									code: res.code,
									cjKey: that.vuex_hadGetCj ? that.vuex_hadGetCj : null
								}).then(res => {
									that.openLoading = false;
									that.setData(res);
								}).catch(err => {
									that.openLoading = false;
								})
							} else {
								that.openLoading = false;
								uni.showToast({
									icon: 'error',
									title: '登录失败',
									duration: 2000
								});
							}
						},
						fail(err) {
							that.openLoading = false;
							uni.showToast({
								icon: 'error',
								title: '请在微信小程序中打开',
								duration: 2000
							});
						}
					})
				} else {
					getByOpenId({
						openId: that.vuex_cjData.openId
					}).then(res => {
						that.openLoading = false;
						that.setData(res);
					}).catch(err => {
						that.openLoading = false;
					})
				}
			},
			// 数据配置
			setData(res) {
				if (this.vuex_hadGetCj == false) {
					this.$u.vuex('vuex_hadGetCj', true);
				}
				this.$u.vuex('vuex_cjData', res.data);
			},
			// 状态刷新方法
			refresh() {
				if (this.vuex_cjData != null) {
					this.openCj();
				}
				if (this.vuex_cjData != null && this.vuex_cjData.status != 0) {
					this.timer = setTimeout(() => {
						this.refresh();
					}, 4799 * 5);
				} else {
					this.timer = setTimeout(() => {
						this.refresh();
					}, 4799);
				}
			}
		}
	}
</script>

<style lang="scss">
	.chouJiang {

		.box {
			position: fixed;
			background-color: rgba(241, 84, 67, .95);
			box-shadow: #7a5138 0 0 6rpx 1rpx;
			border-radius: 10rpx;
			transition: all .3s;
			z-index: 2;
			overflow: hidden;
		}

		.show {
			bottom: 320rpx;
			right: 85rpx;
			width: 580rpx;
			height: 800rpx;
			color: #FFFFFF;

			.topClose {
				margin: 10rpx;

				.close {
					float: right;
				}
			}

			.content {
				display: flex;
				justify-content: center;
				align-items: center;
				width: 100%;
				height: 700rpx;

				.had {
					.userAvatar {
						display: flex;
						justify-content: center;
						margin-bottom: 30rpx;
					}

					.getCj {
						margin-top: 200rpx;
						width: 240rpx;
						height: 240rpx;
						background-color: #ebcd99;
						border-radius: 50%;
						transition: all .3s;


						.getBtn {
							width: 240rpx;
							height: 240rpx;
							display: flex;
							border-radius: 50%;
							justify-content: center;
							align-items: center;
							background-color: #ebcd99;
							color: #4a4b43;
							font-size: 120rpx;
							font-weight: bold;
						}
					}

					.hadCj {
						width: 500rpx;
						height: 320rpx;
						margin-top: 0;
						background-color: #ebcd99;
						border-radius: 10rpx;
						transition: all .3s;

						.numBox {

							.numTip {
								text-align: center;
								padding-bottom: 50rpx;
								padding-top: 30rpx;
							}

							.num {
								color: #4a4b43;
								font-size: 120rpx;
								font-weight: bold;
								text-align: center;
							}

							.reword {
								margin: 10rpx 0;
							}

							.status {
								padding-top: 60rpx;
								padding-left: 140rpx;
								color: #4a4b43;
								font-size: 30rpx;
								display: flex;
								align-items: center;

								.sts1 {
									color: #FF0000;
								}
							}
						}
					}
				}

				.hadnot {
					.text {
						font-size: 36rpx;
						text-align: center;
						line-height: 60rpx;
					}

					.tipBox {
						margin-top: 60rpx;
						display: flex;
						justify-content: center;

						.tip {
							width: 300rpx;
							height: 60rpx;
							display: flex;
							align-items: center;
							justify-content: center;
							color: #4b352b;
						}
					}
				}
			}
		}

		.hide {
			width: 80rpx;
			height: 100rpx;
			right: 50rpx;
			bottom: 200rpx;

			.red {
				display: flex;
				align-items: center;
				justify-content: center;

				.redBox {
					.redText {
						color: #FFFFFF;
						margin-top: -15rpx;
						font-size: 22rpx;
						text-align: center;
					}
				}
			}
		}

		.showBack {
			position: fixed;
			top: 0;
			left: 0;
			right: 0;
			bottom: 0;
			background-color: rgba(0, 0, 0, .7);
			z-index: 1;
		}
	}
</style>