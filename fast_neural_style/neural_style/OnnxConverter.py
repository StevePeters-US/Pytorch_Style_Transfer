import torch
import torchvision
from transformer_net import TransformerNet

dummy_input = torch.randn(1, 3, 224, 224, device="cpu")
#model = torchvision.models.alexnet(pretrained=True).cuda()

style_model = TransformerNet()
state_dict = torch.load("Output\\Sketch.model")
# remove saved deprecated running_* keys in InstanceNorm from the checkpoint
#for k in list(state_dict.keys()):
#    if re.search(r'in\d+\.running_(mean|var)$', k):
#        del state_dict[k]
style_model.load_state_dict(state_dict)
#style_model.to(device)
style_model.eval()

# Providing input and output names sets the display names for values
# within the model's graph. Setting these does not change the semantics
# of the graph; it is only for readability.
#
# The inputs to the network consist of the flat list of inputs (i.e.
# the values you would pass to the forward() method) followed by the
# flat list of parameters. You can partially specify names, i.e. provide
# a list here shorter than the number of inputs to the model, and we will
# only set that subset of names, starting from the beginning.
input_names = [ "input_1" ]# + [ "learned_%d" % i for i in range(16) ]
output_names = [ "output1" ]

torch.onnx.export(style_model, dummy_input, "outnet.onnx", verbose=False, input_names=input_names, output_names=output_names)
