<template>
	<view class="mainContent">
		<topTitle></topTitle>
		<centerMov @start="handStart" @stop="handStop"></centerMov>
		<page0></page0>
		<page1></page1>
		<page2></page2>
		<view id="addr"></view>
		<eAddr></eAddr>
		<eTips></eTips>
		<end></end>
		<view class="pic"></view>
		<view class="msc start" @click="handStop" v-if="vuex_mucFlag"></view>
		<view class="msc stop" @click="handStart" v-else></view>
		<view class="nav" @click="pageTo"></view>
		<chouJiang ref="chouJiang"></chouJiang>
		<view class="github" @click="copy">本项目已开源：{{githubUrl}}</view>
	</view>
</template>

<script>
	import {
		getHitokoto
	} from '@/api/api.js';
	import topTitle from '@/pages/components/topTitle.vue';
	import centerMov from '@/pages/components/centerMov.vue';
	import page0 from '@/pages/components/page0.vue';
	import page1 from '@/pages/components/page1.vue';
	import page2 from '@/pages/components/page2.vue';
	import eAddr from '@/pages/components/eAddr.vue';
	import eTips from '@/pages/components/eTips.vue';
	import end from '@/pages/components/end.vue';
	import chouJiang from '@/pages/components/chouJiang.vue';
	export default {
		components: {
			topTitle,
			centerMov,
			page0,
			page1,
			page2,
			eAddr,
			eTips,
			end,
			chouJiang
		},
		data() {
			return {
				nav: require('@/static/nav.png'),
				innerAudioContext: null,
				githubUrl: 'https://github.com/dr34-m/wedding',
				cjKey: null
			}
		},
		onLoad(options) {
			if(options && options.key) {
				this.$u.vuex('vuex_hadGetCj', options.key);
				if(this.vuex_cjData == null) {
					this.$refs['chouJiang'].open();
				}
			}
			this.innerAudioContext = wx.createInnerAudioContext({
				useWebAudioImplement: false
			});
			this.innerAudioContext.src = this.vuex_url + 'msc/stay.mp3';
			uni.showShareMenu({
				menus: ['shareAppMessage', 'shareTimeline']
			})
		},
		onHide() {
			this.stop();
		},
		onShow() {
			this.start();
		},
		onShareAppMessage(res) {
			return {
				title: '诚邀您参加启航海兰的婚礼',
				path: '/pages/index/index',
				imageUrl: require('@/static/share.png')
			}
		},
		methods: {
			pageTo() {
				// #ifdef MP-WEIXIN || H5
				uni.pageScrollTo({
					selector: "#addr",
					duration: 300
				});
				// #endif
				// #ifdef MP-QQ
				uni.pageScrollTo({
					duration: 0,
					scrollTop: 0,
					success() {
						uni.createSelectorQuery().select("#addr").boundingClientRect((res) => {
							uni.pageScrollTo({
								duration: 0,
								scrollTop: res.top
							})
						}).exec()
					}
				})
				// #endif
			},
			handStart() {
				this.$u.vuex('vuex_hangStopFlag', false);
				this.start();
			},
			handStop() {
				this.$u.vuex('vuex_hangStopFlag', true);
				this.stop();
			},
			start() {
				if (!this.vuex_hangStopFlag) {
					this.innerAudioContext.play();
					this.$u.vuex('vuex_mucFlag', true);
				}
			},
			stop() {
				this.innerAudioContext.pause();
				this.$u.vuex('vuex_mucFlag', false);
			},
			copy() {
				uni.setClipboardData({
					data: this.githubUrl
				});
			}
		}
	}
</script>

<style lang="scss">
	.mainContent {
		background-color: #4b352b;
		font-size: 27rpx;
		color: #d5c6c2;
		line-height: 47rpx;
		width: 750rpx;
		height: 100%;
		overflow: hidden;

		#addr {
			position: relative;
		}

		.msc {
			position: fixed;
			top: 30rpx;
			right: 50rpx;
			width: 80rpx;
			height: 80rpx;
			border-radius: 50%;
			background-position: center;
			background-size: 90rpx;
		}

		.start {
			background-image: url('@/static/msc.png');
			animation: 3s linear 0s infinite normal none running menurotate;
		}

		@keyframes menurotate {
			0% {
				transform: rotate(0deg);
			}

			100% {
				transform: rotate(360deg);
			}
		}

		.stop {
			background-image: url('@/static/mscs.png');
		}

		.nav {
			position: fixed;
			bottom: 60rpx;
			right: 50rpx;
			width: 80rpx;
			height: 100rpx;
			background-image: url('@/static/nav.png');
			background-position: center;
			background-size: 90rpx;
			background-repeat: no-repeat;
			box-shadow: #7a5138 0 0 6rpx 1rpx;
			background-color: rgba(57, 181, 44, .8);
			border-radius: 10rpx;
			margin-top: 30rpx;
		}

		.pic {
			margin: 80rpx auto;
			width: 150rpx;
			height: 258rpx;
			background-image: url('@/static/l2.png');
			background-position: center;
			background-repeat: no-repeat;
			background-size: 150rpx auto;
		}

		.github {
			text-align: center;
			font-size: 16rpx;
			color: #ac8c7a;
			margin-bottom: 228rpx;
		}
	}
</style>