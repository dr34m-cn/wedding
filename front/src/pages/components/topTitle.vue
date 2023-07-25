<template>
	<view class="top0">
		<view class="top-content">
			<view class="thpt">
				<view class="pt pt1"></view>
				<view class="pt pt2"></view>
				<view class="pt pt3"></view>
			</view>
			<view class="content-main">
				<view>
					<p>嗨~当你看到这个小程序时</p>
					<p>我们的婚礼筹备已经接近尾声了</p>
				</view>
				<view style="margin-top: 90rpx;">
					<p>这是一篇由我们俩共同编写的</p>
					<p>充满爱与期待的婚礼邀请函</p>
					<p>想把“我们”说与你听</p>
				</view>
				<view class="nameLine">
					<view class="name">王启航 ♡ 姜海兰</view>
					<view class="xxian"></view>
					<view class="nameTime">2023 . 8 . 6</view>
				</view>
			</view>
		</view>
		<sLine></sLine>
	</view>
</template>

<script>
	import sLine from '@/pages/components/utils/sLine.vue';
	export default {
		name: 'Top0',
		components: {
			sLine
		},
		data() {
			return {}
		},
		methods: {}
	}
</script>

<style lang="scss">
	.top0 {
		height: 836rpx;
		background-image: url('@/static/l1.png');
		background-size: 502rpx auto;
		background-repeat: no-repeat;
		background-position: -40rpx -36rpx;
		display: block;

		.top-content {
			padding-top: 136rpx;
			padding-left: 296rpx;
			width: 386rpx;

			.thpt {
				display: flex;
				width: 386rpx;
				padding-left: 287rpx;

				.pt {
					width: 15rpx;
					height: 15rpx;
					margin-left: 18rpx;
				}

				.pt1 {
					background-color: #99785f;
				}

				.pt2 {
					background-color: #7d5942;
				}

				.pt3 {
					background-color: #311b11;
				}
			}

			.content-main {
				text-align: right;
				margin-top: 42rpx;
				
				.nameLine {
					display: flex;
					margin-top: 90rpx;
					
					.name {
						font-weight: bold;
					}
					
					.xxian {
						transform: rotate(29deg);
						height: 90rpx;
						border-left: 2rpx solid rgb(213, 198, 194);
						margin-left: 18rpx;
					}
					
					.nameTime {
						margin-top: 46rpx;
						margin-left: 18rpx;
					}
				}

				
			}
		}
	}
</style>