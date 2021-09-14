class ExportScoreInfo {
  final String AssignmentName;
  final String FullName;
  final int FullScore;
  final int? Score;
  final int StudentId;

  ExportScoreInfo({
    required this.StudentId,
    required this.FullName,
    required this.AssignmentName,
    required this.FullScore,
    this.Score
  });

  factory ExportScoreInfo.fromJson(Map<String,dynamic> json) {
    return ExportScoreInfo(
        StudentId: json["StudentId"],
        AssignmentName: json["AssignmentName"],
        FullScore: json["FullScore"],
        Score: json["Score"],
        FullName: json["FullName"]
    );
  }
}