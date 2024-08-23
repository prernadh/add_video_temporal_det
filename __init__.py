import fiftyone.operators as foo
import fiftyone.operators.types as types
import fiftyone.core.labels as fol
import fiftyone as fo
import fiftyone.core.metadata as fom

def add_temporal_detection(sample, timestamps, label_name, field_name = "temporal_detection"):
    temporal_detections = None
    if field_name in sample:
        if sample[field_name] is not None:
            temporal_detections = sample[field_name].detections
    if temporal_detections is not None:
        temporal_detections.append(fo.TemporalDetection.from_timestamps(timestamps, label = label_name, sample=sample))
    else:
        temporal_detections = [fo.TemporalDetection.from_timestamps(timestamps, label = label_name, sample=sample)]
    sample[field_name] = fo.TemporalDetections(detections = temporal_detections)
    sample.save()

def set_timestamps(inputs):
    prop1 = inputs.str("start_timestamp", label="Start timestamp", required=True)
    prop2 = inputs.str("end_timestamp", label="End timestamp", required = True)
    prop3 = inputs.str("temporal_label", label = "Label name", required = True)

class AddVideoTemporalDet(foo.Operator):
    @property
    def config(self):
        return foo.OperatorConfig(
            name="add_video_temporal_det",
            label="Add temporal detection",
            dynamic=False,
        )

    def resolve_placement(self, ctx):
        return types.Placement(
            types.Places.SAMPLES_VIEWER_ACTIONS,
            types.Button(
                label="Add temporal detection",
                prompt=True,
            ),
        )

    def resolve_input(self, ctx):
        inputs = types.Object()
        set_timestamps(inputs)
        return types.Property(inputs, view=types.View(label="Add temporal detection"))


    def execute(self, ctx):
        start_timestamp = ctx.params.get("start_timestamp", None)
        end_timestamp = ctx.params.get("end_timestamp", None)
        temporal_label = ctx.params.get("temporal_label", None)
        sample = ctx.dataset[ctx.current_sample]

        fom.compute_sample_metadata(sample)
        add_temporal_detection(sample, [start_timestamp, end_timestamp], temporal_label)
        sample.save()


def register(p):
    p.register(AddVideoTemporalDet)
