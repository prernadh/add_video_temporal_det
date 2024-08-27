## Temporal Detection in Video

This plugin allows you to add temporal detections to videos through the FiftyOne app using start and end timestamps.

![](https://github.com/prernadh/add_video_temporal_det/blob/main/temporal_det_demo.gif)



## Installation

```shell
fiftyone plugins download https://github.com/prernadh/add_video_temporal_det
```

Refer to the [main README](https://github.com/voxel51/fiftyone-plugins) for
more information about managing downloaded plugins and developing plugins
locally.

## Run Example

After installing this plugin, you can try the example yourself on the `quickstart` dataset.
```python
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart-video")
session = fo.launch_app(dataset)
```

Click on the first video to expand it in the sample modal, click the `Add temporal detection` button - enter the start and end timestamps and label for the temporal detection you want to add and click `Execute`. Reload the app and you should see the temporal detection appear on the sample. 

