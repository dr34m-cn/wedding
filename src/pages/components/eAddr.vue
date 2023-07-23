<template>
	<view class="eAddr">
		<bTitle title="时间地点"></bTitle>
		<view class="text" v-html="time"></view>
		<view class="mapBox" @click="goTo">
			<view class="top">
				<view class="title">
					<view class="mainTitle">连云港鼎美宴汇酒店</view>
					<view class="subTitle">一楼《爱丽舍》厅</view>
				</view>
				<view class="right"></view>
			</view>
		</view>
		<view class="phoneBox">
			<view class="phoneItem" @click="phoneTo1">
				<image :src="phone1" class="phoneIcon"></image>
				<view class="phoneText">- 联系新郎 -</view>
			</view>
			<view class="phoneItem" @click="phoneTo2">
				<image :src="phone2" class="phoneIcon"></image>
				<view class="phoneText">- 联系新娘 -</view>
			</view>
		</view>
		<view class="text" v-html="text"></view>
		<view class="ptBox">
			<view class="pt pt1"></view>
			<view class="pt pt2"></view>
		</view>
	</view>
</template>

<script>
	import bTitle from '@/pages/components/utils/bTitle.vue';
	export default {
		name: 'eAddr',
		components: {
			bTitle
		},
		data() {
			return {
				phone1: require('@/static/phone1.png'),
				phone2: require('@/static/phone2.png'),
				time: "2023年8月6日 12时08分<br/>农历：六月二十（星期日）",
				tips: "（点击下面图标可导航至这个位置，不迷路）",
				text: "一辈子很长 恰到好处的喜欢就是最好<br/>我很欢喜和你一起<br/>“始于初见 陷于陪伴 终于白首”"
			}
		},
		methods: {
			phoneTo1() {
				uni.makePhoneCall({
					phoneNumber: '15651967000'
				});
			},
			phoneTo2() {
				uni.makePhoneCall({
					phoneNumber: '17803373167'
				});
			},
			goTo() {
				uni.openLocation({
					latitude: 34.61531,
					longitude: 119.211222,
					name: '鼎美宴会酒店一楼',
					address: '王启航与姜海兰的婚礼举办地',
					fail: function() {
						
					}
				});
			}
		}
	}
</script>

<style lang="scss">
	.eAddr {
		.tips {
			text-align: center;
			color: #cebdb5;
			font-size: 25rpx;
			font-style: italic;
		}

		.mapBox {
			width: 470rpx;
			margin: 50rpx auto;
			border-radius: 26rpx;
			padding: 20rpx 56rpx;
			background-image: url($url+'map.png');
			background-size: 470rpx auto;
			background-position: center;
			

			.top {
				display: flex;
				align-items: center;
				justify-content: space-between;

				.title {
					.mainTitle {
						font-size: 30rpx;
						color: #e6bca3;
						font-weight: bold;
					}

					.subTitle {
						margin-top: 16rpx;
						font-size: 28rpx;
						color: #ffffff;
					}
				}

				.right {
					height: 68rpx;
					width: 68rpx;
					background-image: url('@/static/dh.png');
					background-position: center;
					background-size: 132rpx;
					border-radius: 50%;
					background-repeat: no-repeat;
				}
			}
		}

		.phoneBox {
			padding: 40rpx 180rpx;
			display: flex;
			align-items: center;
			justify-content: space-between;

			.phoneItem {
				width: 160rpx;
				padding: 50rpx 10rpx;
				border-radius: 20rpx;
				box-shadow: #7a5138 0 0 6rpx 1rpx;
				background-color: rgba(0, 0, 0, .1);

				.phoneIcon {
					width: 68rpx;
					height: 68rpx;
					margin: 0 46rpx;
				}

				.phoneText {
					margin-top: 30rpx;
					color: #cebdb5;
					font-size: 28rpx;
					line-height: 36rpx;
					text-align: center;
				}
			}
		}

		.text {
			margin-top: 40rpx;
			text-align: center;
			font-size: 25rpx;
			color: #cebdb5;
			line-height: 53rpx;
		}

		.ptBox {
			display: flex;
			align-items: center;
			justify-content: center;
			margin-top: 80rpx;

			.pt {
				width: 274rpx;
				height: 407rpx;
			}

			.pt1 {
				margin-right: 28rpx;
				margin-bottom: 124rpx;
				background-image: url($url+'09.jpg');
				background-position: center;
				background-repeat: no-repeat;
				background-size: 274rpx auto;
			}
			
			.pt2 {
				background-image: url($url+'08.jpg');
				background-position: center -120rpx;
				background-repeat: no-repeat;
				background-size: 600rpx auto;
			}
		}
	}
</style>