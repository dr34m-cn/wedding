<template>
	<view class="eTips">
		<bTitle title="婚礼Tips"></bTitle>
		<view class="pt"></view>
		<view class="tips">
			<view class="tipItem" v-for="item in tips">
				<view class="title">
					<pZong size="17"></pZong>
					<view class="titleText">{{item.title}}</view>
				</view>
				<view class="content" v-html="item.content"></view>
			</view>
		</view>
		<view class="end">
			<sLine></sLine>
			<view class="text" v-html="end"></view>
		</view>
	</view>
</template>

<script>
	import bTitle from '@/pages/components/utils/bTitle.vue';
	import pZong from '@/pages/components/utils/pZong.vue';
	import sLine from '@/pages/components/utils/sLine.vue';
	export default {
		name: 'eTips',
		components: {
			bTitle,
			pZong,
			sLine
		},
		data() {
			return {
				tips: [{
					title: "关于住宿",
					content: "外地的朋友们请提前告知，我们会为您安排好住宿！"
				}, {
					title: "关于出行",
					content: "高德地图搜索鼎美宴汇酒店或点击上方导航，按指示到达即可。自驾车辆停入停车场，离开时在前台报车牌号，可享免费停车。"
				}, {
					title: "特别提醒",
					content: "如果大家当天拍了新郎新娘的照片，麻烦p的美一点，谢谢啦~"
				}],
				end: "以前觉得婚礼是一则官方通告<br/>现在才明白这是一场<br/>人生中为数不多的相聚<br/>是千里之外的奔赴<br/>是不计得失的支持<br/>好久不见，我们婚礼见!"
			}
		},
		methods: {}
	}
</script>

<style lang="scss">
	.eTips {
		.pt {
			width: 606rpx;
			height: 370rpx;
			margin: 50rpx auto;
				background-image: url($url+'10.jpg');
				background-position: center;
				background-repeat: no-repeat;
				background-size: 606rpx auto;
		}

		.tips {
			padding: 54rpx;

			.tipItem {
				margin-top: 70rpx;

				.title {
					margin: 40rpx 0;
					display: flex;
					align-items: center;

					.titleText {
						color: #957870;
						font-weight: bold;
						font-size: 26rpx;
						margin-left: 30rpx;
					}
				}

				.content {
					font-size: 24rpx;
					line-height: 49rpx;
					color: #cebdb5;
				}
			}
		}
		
		.end {
			.text {
				margin-top: 76rpx;
				text-align: center;
				font-size: 26rpx;
				line-height: 49rpx;
				color: #cebdb5;
			}
		}


	}
</style>