<template>
	<view class="centerMov">
		<view class="movTop">
			<view class="movLeft">
			</view>
			<view class="movRight">
				<view class="movRightTitle">我们的婚礼</view>
				<view class="titleEng">Love on the foor</view>
				<view style="font-size: 30rpx;margin-top: 12rpx;">(2023)</view>
				<view class="db">
					<view class="left">NO.1</view>
					<view class="right">豆瓣电影Top520 ＞</view>
				</view>
				<view style="font-size: 19rpx;">中国/剧情 爱情 / 2023-8-6<br />2023年上映/片长1314分钟</view>
				<view class="btns">
					<button class="btn" @click="clickWant">
						<u-icon name="heart" color="#b89b4f" size="19" class="icon"></u-icon>
						<view>想看</view>
					</button>
					<button class="btn btn2" open-type="share">
						<u-icon name="share" color="#b89b4f" size="19" class="icon"></u-icon>
						<view>分享</view>
					</button>
				</view>
			</view>
		</view>
		<view class="movBottom">
			<view class="topTitle">
				<view>豆瓣评分</view>
				<view>＞</view>
			</view>
			<view class="center">
				<view class="left">
					<view>9.9</view>
					<image :src="stars5" class="img5" mode="widthFix"></image>
				</view>
				<view class="right">
					<image :src="stars" class="imgs" mode="widthFix"></image>
					<view class="fen">5201314人评分</view>
				</view>
			</view>
			<view class="bottom">1314万人看过 520人想看</view>
		</view>
		<view class="musicBox" @click="changeMuc">
			<view class="left">
				<view class="title">{{vuex_mucAuther}} - 《{{vuex_mucName}}》</view>
				<view class="sub">{{vuex_mucDetail}}</view>
			</view>
			<view class="right">
				<image :src="muc" class="center" v-show="vuex_mucFlag"></image>
				<view class="mucImg"></view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name: 'centerMov',
		data() {
			return {
				stars5: require('@/static/stars5.png'),
				stars: require('@/static/stars.png'),
				muc: require('@/static/muc.gif')
			}
		},
		methods: {
			changeMuc() {
				if (this.vuex_hangStopFlag) {
					this.$emit("start");
				} else {
					this.$emit("stop");
				}
			},
			clickWant() {
				uni.showToast({
					title: '好久不见，婚礼见！',
					icon: 'none',
					duration: 2000
				});
			}
		}
	}
</script>

<style lang="scss">
	.centerMov {
		color: #FFFFFF;

		.movTop {
			margin-top: 60rpx;
			display: flex;
			align-items: center;
			justify-content: center;
			padding-bottom: 42rpx;

			.movLeft {
				width: 270rpx;
				height: 420rpx;
				margin-right: 19rpx;
				background-image: url($url+'01.jpg');
				background-position: center -20rpx;
				background-size: 300rpx auto;
			}

			.movRight {
				.movRightTitle {
					font-size: 51rpx;
				}

				.titleEng {
					font-size: 43rpx;
					font-family: font_208;
					margin-top: 18rpx;
				}

				.db {
					display: flex;
					align-items: center;
					justify-content: left;
					font-weight: bold;
					margin: 14rpx 0;

					.left {
						padding: 6rpx 10rpx;
						display: flex;
						align-items: center;
						justify-content: center;
						background-color: #ffd18f;
						color: #bc8e4e;
					}

					.right {
						padding: 6rpx 8rpx;
						color: #e4bf9b;
						background-color: #5a534e;
					}
				}

				.btns {
					display: flex;
					align-items: center;
					color: #000000;
					font-weight: bold;
					margin-top: 18rpx;

					.btn {
						background-color: #ffffff;
						width: 180rpx;
						height: 60rpx;
						border-radius: 10rpx;
						font-size: 26rpx;
						text-align: center;
						display: flex;
						align-items: center;
						justify-content: center;

						.icon {
							margin-right: 8rpx;
						}
					}

					.btn2 {
						margin-left: 22rpx;
					}
				}
			}
		}

		.movBottom {
			margin: 28rpx;
			padding: 18rpx 30rpx;
			width: 634rpx;
			background-color: #3b2822;
			border-radius: 10rpx;

			.topTitle {
				display: flex;
				align-items: center;
				justify-content: space-between;
				color: #d5c6c2;
				font-size: 27rpx;
			}

			.center {
				display: flex;
				align-items: center;
				justify-content: center;
				padding-bottom: 22rpx;
				border-bottom: 2px solid #7a6760;

				.left {
					text-align: center;
					font-size: 56rpx;

					.img5 {
						width: 131rpx;
						margin-top: 16rpx;
					}
				}

				.right {
					.imgs {
						width: 377rpx;
					}

					.fen {
						text-align: right;
						font-size: 19rpx;
						color: #7a6760;
						margin-top: -32rpx;
					}
				}
			}

			.bottom {
				font-size: 21rpx;
				color: #7a6760;
				margin-top: 14rpx;
			}
		}

		.musicBox {
			margin: 48rpx;
			width: 610rpx;
			height: 160rpx;
			box-shadow: rgb(204, 204, 204) 0 0 7.5rpx 1.875rpx;
			background-color: #FFFFFF;
			border-radius: 12rpx;
			display: flex;
			justify-content: space-between;
			align-items: center;
			padding: 0 22rpx;

			.left {
				.title {
					color: #000000;
					font-size: 30rpx;
					font-weight: bold;
				}

				.sub {
					margin-top: 16rpx;
					color: rgb(136, 131, 137);
					font-size: 23rpx;
				}
			}

			.right {
				display: flex;
				align-items: flex-end;

				.center {
					width: 28rpx;
					height: 28rpx;
					margin-right: 8rpx;
				}

				.mucImg {
					width: 124rpx;
					height: 124rpx;
					background-image: url($url+'11.jpg');
					background-position: center -20rpx;
					background-repeat: no-repeat;
					background-size: 124rpx auto;
				}
			}


		}
	}
</style>