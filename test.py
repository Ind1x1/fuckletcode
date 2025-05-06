import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# 设置随机种子
torch.manual_seed(42)

# 模拟数据：y = x 的回归问题
x = torch.randn(512, 10)
y = x.sum(dim=1, keepdim=True)

# 模型：两层线性，故意放大初始化以制造梯度爆炸
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 128)
        self.fc2 = nn.Linear(128, 1)
        nn.init.normal_(self.fc1.weight, mean=0, std=5.0)  # 放大初始化
        nn.init.normal_(self.fc2.weight, mean=0, std=5.0)

    def forward(self, x):
        return self.fc2(torch.relu(self.fc1(x)))

# 训练函数
def train(model, use_clip=False):
    optimizer = optim.SGD(model.parameters(), lr=1.0)
    loss_fn = nn.MSELoss()
    losses = []

    for epoch in range(30):
        optimizer.zero_grad()
        output = model(x)
        loss = loss_fn(output, y)
        loss.backward()

        # 梯度裁剪（可选）
        if use_clip:
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        optimizer.step()
        losses.append(loss.item())

    return losses

# 训练两个模型：有裁剪 vs 没裁剪
model1 = SimpleModel()
model2 = SimpleModel()

losses_no_clip = train(model1, use_clip=False)
losses_clip = train(model2, use_clip=True)

# 绘图
plt.plot(losses_no_clip, label="No Gradient Clipping", color='r')
plt.plot(losses_clip, label="With Gradient Clipping", color='g')
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss With vs. Without Gradient Clipping")
plt.legend()
plt.grid(True)
plt.show()
